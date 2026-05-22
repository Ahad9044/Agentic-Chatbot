import html
from typing import Literal

import streamlit as st

from src.langgraphagenticai.ui.streamlitui.components.scroll import scroll_to_latest_message

MessageRole = Literal["user", "assistant", "tool"]

ROLE_LABELS = {
    "user": ("You", "conv-label-user"),
    "assistant": ("Assistant", "conv-label-assistant"),
    "tool": ("Tool", "conv-label-tool"),
}


def clear_chat_on_usecase_change(usecase: str) -> None:
    if st.session_state.get("_last_usecase") != usecase:
        st.session_state.chat_history = []
        st.session_state.messages = []
        st.session_state._last_usecase = usecase


def append_history(role: MessageRole, content: str) -> None:
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    st.session_state.chat_history.append({"role": role, "content": content})
    st.session_state.scroll_to_bottom = True


def has_chat_history() -> bool:
    return bool(st.session_state.get("chat_history"))


def _render_message_in_thread(role: str, content: str, show_divider: bool) -> None:
    if show_divider:
        st.markdown('<div class="conv-divider"></div>', unsafe_allow_html=True)

    label, label_class = ROLE_LABELS.get(role, ("Message", "conv-label-assistant"))
    st.markdown(
        f'<p class="conv-label {label_class}">{html.escape(label)}</p>',
        unsafe_allow_html=True,
    )

    if role == "tool":
        st.code(content[:3000] + ("…" if len(content) > 3000 else ""), language=None)
    else:
        st.markdown(content)


def render_chat_history() -> None:
    history = st.session_state.get("chat_history", [])
    for i, msg in enumerate(history):
        _render_message_in_thread(msg["role"], msg["content"], show_divider=i > 0)
    st.markdown('<div class="conv-scroll-anchor"></div>', unsafe_allow_html=True)


def render_loading_indicator(label: str = "Agent is thinking") -> None:
    st.markdown(
        f"""
        <div class="loading-wrap">
            <p>{html.escape(label)}</p>
            <div class="loading-dots">
                <span></span><span></span><span></span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_conversation_section() -> None:
    st.markdown(
        '<p class="section-title">Conversation</p>',
        unsafe_allow_html=True,
    )

    with st.container(border=True):
        render_chat_history()
