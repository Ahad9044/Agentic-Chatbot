import streamlit as st

from src.langgraphagenticai.ui.uiconfigfile import Config
from src.langgraphagenticai.ui.streamlitui.theme.styles import inject_global_styles
from src.langgraphagenticai.ui.streamlitui.components.session import init_app_session
from src.langgraphagenticai.ui.streamlitui.components.header import render_header, render_status_bar
from src.langgraphagenticai.ui.streamlitui.components.sidebar import render_sidebar
from src.langgraphagenticai.ui.streamlitui.components.chat_panel import (
    clear_chat_on_usecase_change,
    render_conversation_section,
    has_chat_history,
)
from src.langgraphagenticai.ui.streamlitui.components.welcome import render_welcome_screen


class LoadStreamlitUI:
    """Orchestrates theme injection, sidebar, header, and main content shell."""

    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    def load_streamlit_ui(self):
        page_title = self.config.get_page_title() or "Agentic AI"

        st.set_page_config(
            page_title=page_title,
            page_icon="🤖",
            layout="wide",
            initial_sidebar_state="expanded",
        )

        init_app_session()
        inject_global_styles()

        self.user_controls = render_sidebar(self.config)
        usecase = (self.user_controls.get("selected_usecase") or "").strip()
        clear_chat_on_usecase_change(usecase)

        render_header(page_title)

        if has_chat_history():
            render_status_bar(self.user_controls)
            render_conversation_section()
        else:
            render_welcome_screen(usecase)

        return self.user_controls
