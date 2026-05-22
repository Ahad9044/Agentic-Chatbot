import html

import streamlit as st

from src.langgraphagenticai.ui.streamlitui.theme.constants import get_usecase_meta


def render_header(page_title: str) -> None:
    safe_title = html.escape(page_title.strip())

    st.markdown(
        f"""
        <header class="site-header">
            <div class="site-header-inner">
                <div class="site-brand">
                    <span class="site-logo" aria-hidden="true">✦</span>
                    <h1 class="site-name">{safe_title}</h1>
                </div>
                <p class="site-tagline">Chatbot · Web Search · News Digest</p>
            </div>
        </header>
        """,
        unsafe_allow_html=True,
    )


def render_status_bar(user_controls: dict) -> None:
    usecase = (user_controls.get("selected_usecase") or "—").strip()
    model = html.escape((user_controls.get("selected_groq_model") or "—").strip())
    meta = get_usecase_meta(usecase)

    groq_ok = bool(user_controls.get("GROQ_API_KEY"))
    tavily_needed = usecase in ("Chatbot With Web", "AI News")
    tavily_ok = bool(user_controls.get("TAVILY_API_KEY")) if tavily_needed else True
    ready = groq_ok and tavily_ok
    status_class = "ready" if ready else "pending"
    status_text = "Online" if ready else "Awaiting keys"

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(
            f"""
            <div class="metric-card" style="animation-delay:0.05s">
                <div class="label">Agent mode</div>
                <div class="value">{meta['icon']} {html.escape(usecase)}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            f"""
            <div class="metric-card" style="animation-delay:0.12s">
                <div class="label">LLM model</div>
                <div class="value">{model}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            f"""
            <div class="metric-card" style="animation-delay:0.2s">
                <div class="label">System</div>
                <div class="value"><span class="status-pill {status_class}">{status_text}</span></div>
            </div>
            """,
            unsafe_allow_html=True,
        )
