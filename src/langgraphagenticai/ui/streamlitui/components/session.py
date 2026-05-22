import streamlit as st


def init_app_session() -> None:
    defaults = {
        "chat_history": [],
        "messages": [],
        "timeframe": "",
        "IsFetchButtonClicked": False,
        "GROQ_API_KEY": "",
        "TAVILY_API_KEY": "",
        "_last_usecase": None,
        "scroll_to_bottom": False,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value
