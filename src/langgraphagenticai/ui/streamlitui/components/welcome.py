import streamlit as st


def render_welcome_screen(usecase: str) -> None:
    """Claude/Gemini-style empty state: centered greeting only."""
    if usecase == "AI News":
        greeting = "How can I help you?"
        sub = "Select a time frame in the sidebar, then fetch the latest AI news."
    else:
        greeting = "How can I help you?"
        sub = ""

    sub_html = f'<p class="welcome-sub">{sub}</p>' if sub else ""

    st.markdown(
        f"""
        <div class="welcome-screen">
            <h2 class="welcome-greeting">{greeting}</h2>
            {sub_html}
        </div>
        """,
        unsafe_allow_html=True,
    )
