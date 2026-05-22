import os

import streamlit as st

from src.langgraphagenticai.ui.uiconfigfile import Config
from src.langgraphagenticai.ui.streamlitui.theme.constants import USECASE_META


def _normalize_usecase(value: str) -> str:
    return (value or "").strip()


def render_sidebar(config: Config) -> dict:
    user_controls: dict = {}

    with st.sidebar:
        st.markdown(
            """
            <div class="sidebar-brand">
                <div class="logo-wrap"> ✨ </div>
                <h2>Agent Selection Panel</h2>
                <span>Configure stack · Run agents</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        with st.expander("🧠 LLM Provider", expanded=True):
            llm_options = config.get_llm_options()
            user_controls["selected_llm"] = st.selectbox(
                "Provider",
                llm_options,
                label_visibility="collapsed",
            )
            if user_controls["selected_llm"] == "Groq":
                user_controls["selected_groq_model"] = st.selectbox(
                    "Groq model",
                    config.get_groq_model_options(),
                )
                user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input(
                    "Groq API key",
                    type="password",
                    placeholder="gsk_••••••••",
                )
                if not user_controls["GROQ_API_KEY"]:
                    st.caption("[Get Groq API key →](https://console.groq.com/keys)")

        with st.expander("🎯 Agent mode", expanded=True):
            raw_options = [_normalize_usecase(o) for o in config.get_usecase_options()]
            choice = st.radio(
                "Use case",
                raw_options,
                format_func=lambda x: f"{USECASE_META.get(x, {}).get('icon', '🤖')}  {x}",
                label_visibility="collapsed",
            )
            user_controls["selected_usecase"] = _normalize_usecase(choice)

        if user_controls["selected_usecase"] in ("Chatbot With Web", "AI News"):
            with st.expander("🔑 Tavily Search", expanded=True):
                os.environ["TAVILY_API_KEY"] = user_controls["TAVILY_API_KEY"] = (
                    st.session_state["TAVILY_API_KEY"]
                ) = st.text_input(
                    "Tavily API key",
                    type="password",
                    placeholder="tvly-••••••••",
                )
                if not user_controls["TAVILY_API_KEY"]:
                    st.caption("[Get Tavily API key →](https://app.tavily.com/home)")

        if user_controls["selected_usecase"] == "AI News":
            st.markdown("---")
            st.markdown("**📰 News digest**")
            time_frame = st.selectbox(
                "Time frame",
                ["Daily", "Weekly", "Monthly"],
                index=0,
            )
            if st.button(
                "🔍 Fetch latest AI news",
                type="primary",
                use_container_width=True,
            ):
                st.session_state.IsFetchButtonClicked = True
                st.session_state.timeframe = time_frame

        st.markdown("---")
        st.caption(" Made with ❤️ by Ahad")

    return user_controls
