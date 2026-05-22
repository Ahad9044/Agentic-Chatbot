import streamlit as st

from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMS.groqllm import GroqLLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit
from src.langgraphagenticai.ui.streamlitui.components.chat_panel import has_chat_history
from src.langgraphagenticai.ui.streamlitui.components.scroll import scroll_to_latest_message


def load_langgraph_agenticai_app():
    """Loads and runs the LangGraph AgenticAI application with Streamlit UI."""
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Failed to load UI controls.")
        return

    usecase = (user_input.get("selected_usecase") or "").strip()

    # Chat input directly below welcome (empty) or below conversation (has history)
    st.markdown('<div class="chat-input-zone">', unsafe_allow_html=True)

    if st.session_state.IsFetchButtonClicked:
        user_message = st.session_state.timeframe
    else:
        placeholder = "Ask anything…" if not has_chat_history() else "Message your agent…"
        user_message = st.chat_input(
            placeholder,
            disabled=usecase == "AI News",
        )

    st.markdown("</div>", unsafe_allow_html=True)

    if has_chat_history() or st.session_state.get("scroll_to_bottom"):
        scroll_to_latest_message()
        st.session_state.scroll_to_bottom = False

    if user_message:
        try:
            obj_llm_config = GroqLLM(user_contols_input=user_input)
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("LLM model could not be initialized.")
                return

            if not usecase:
                st.error("No use case selected.")
                return

            graph_builder = GraphBuilder(model)
            graph = graph_builder.setup_graph(usecase)
            DisplayResultStreamlit(usecase, graph, user_message).display_result_on_ui()

        except Exception as e:
            st.error(f"Error: {e}")
