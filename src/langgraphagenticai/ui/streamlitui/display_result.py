import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage

from src.langgraphagenticai.ui.streamlitui.components.chat_panel import (
    append_history,
    render_loading_indicator,
)


class DisplayResultStreamlit:
    def __init__(self, usecase, graph, user_message):
        self.usecase = (usecase or "").strip()
        self.graph = graph
        self.user_message = user_message

    def _ensure_history(self) -> None:
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []
        if "messages" not in st.session_state:
            st.session_state.messages = []

    def display_result_on_ui(self):
        self._ensure_history()
        usecase = self.usecase
        graph = self.graph
        user_message = self.user_message

        if usecase == "Basic Chatbot":
            st.session_state.messages.append(HumanMessage(content=user_message))
            append_history("user", user_message)

            placeholder = st.empty()
            with placeholder.container():
                render_loading_indicator("Streaming response from Groq…")
            assistant_text = ""
            for event in graph.stream({"messages": st.session_state.messages}):
                for value in event.values():
                    assistant_text = getattr(
                        value["messages"], "content", str(value["messages"])
                    )
            placeholder.empty()

            append_history("assistant", assistant_text)
            st.session_state.messages.append(AIMessage(content=assistant_text))
            st.rerun()

        elif usecase == "Chatbot With Web":
            st.session_state.messages.append(HumanMessage(content=user_message))
            append_history("user", user_message)

            with st.spinner(""):
                render_loading_indicator("Searching the web & reasoning…")
                res = graph.invoke({"messages": st.session_state.messages})

            for message in res["messages"]:
                if isinstance(message, ToolMessage):
                    append_history("tool", message.content)
                elif isinstance(message, AIMessage) and message.content:
                    append_history("assistant", message.content)
                    st.session_state.messages.append(message)
            st.rerun()

        elif usecase == "AI News":
            frequency = user_message
            append_history("user", f"Generate **{frequency}** AI news digest")

            with st.spinner(""):
                render_loading_indicator("Running fetch → summarize → save pipeline…")
                graph.invoke({"messages": frequency})

            try:
                ai_news_path = f"./AINews/{frequency.lower()}_summary.md"
                with open(ai_news_path, "r", encoding="utf-8") as file:
                    markdown_content = file.read()
                append_history("assistant", markdown_content)
            except FileNotFoundError:
                st.error(f"News not generated or file not found: {ai_news_path}")
            except Exception as e:
                st.error(f"An error occurred: {e}")

            st.session_state.IsFetchButtonClicked = False
            st.rerun()
