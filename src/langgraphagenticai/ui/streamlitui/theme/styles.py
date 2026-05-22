"""Readable dark theme — elevated panels, high contrast, visible widgets."""

GLOBAL_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

/* ── Base: readable slate-blue (not pure black) ── */
.stApp {
    background: linear-gradient(165deg,
        #1e2d4d 0%,
        #2a3f6b 35%,
        #243352 65%,
        #1a2744 100%) !important;
    font-family: 'Plus Jakarta Sans', system-ui, sans-serif;
    color: #f1f5f9 !important;
}

.main .block-container,
[data-testid="stAppViewContainer"] .main .block-container {
    padding: 1.5rem 2rem 3rem;
    max-width: 1100px;
}

/* All default Streamlit text — force light */
.stApp p, .stApp span, .stApp label, .stApp li,
.stMarkdown, .stMarkdown p,
[data-testid="stMarkdownContainer"] p,
[data-testid="stWidgetLabel"] p,
.stCaption, .stCaption p {
    color: #e2e8f0 !important;
}

/* ── Sidebar: solid elevated panel ── */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #2d3a5c 0%, #243352 100%) !important;
    border-right: 1px solid #4a5d82 !important;
}
section[data-testid="stSidebar"] > div,
section[data-testid="stSidebar"] [data-testid="stSidebarContent"] {
    background: transparent !important;
}
section[data-testid="stSidebar"] .stMarkdown,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] p {
    color: #f1f5f9 !important;
}

/* ── Website-style top header (rounded card) ── */
.site-header {
    width: 100%;
    margin: 0 0 1.5rem 0;
    padding: 0;
    background: linear-gradient(180deg, #1a2744 0%, #243352 100%);
    border: 1px solid #5a6fa0;
    border-radius: 18px;
    box-shadow: 0 8px 28px rgba(0, 0, 0, 0.22);
    overflow: hidden;
}
.site-header-inner {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    gap: 0.75rem 1.5rem;
    padding: 1rem 2rem;
    max-width: 1100px;
    margin: 0 auto;
}
.site-brand {
    display: flex;
    align-items: center;
    gap: 0.85rem;
    text-decoration: none !important;
    cursor: default;
}
.site-logo {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 44px;
    height: 44px;
    border-radius: 12px;
    font-size: 1.25rem;
    font-weight: 800;
    color: #fff !important;
    background: linear-gradient(135deg, #6366f1, #06b6d4);
    box-shadow: 0 4px 14px rgba(99, 102, 241, 0.45);
}
.site-name {
    margin: 0 !important;
    font-size: 1.5rem !important;
    font-weight: 800 !important;
    letter-spacing: -0.02em;
    line-height: 1.2 !important;
    color: #ffffff !important;
    -webkit-text-fill-color: #ffffff !important;
}
.site-tagline {
    margin: 0 !important;
    font-size: 0.8rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: #a5b4fc !important;
    padding: 0.45rem 1rem;
    background: rgba(99, 102, 241, 0.15);
    border: 1px solid rgba(129, 140, 248, 0.35);
    border-radius: 999px;
    white-space: nowrap;
}

/* ── Metric cards ── */
.metric-card {
    background: linear-gradient(145deg, #3d4f7c, #35466e);
    border: 1px solid #5a6fa0;
    border-radius: 14px;
    padding: 1rem;
    text-align: center;
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
}
.metric-card .label {
    font-size: 0.65rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #94a3b8 !important;
    margin-bottom: 0.35rem;
}
.metric-card .value {
    font-size: 0.92rem;
    font-weight: 600;
    color: #ffffff !important;
}

/* ── Use case panel ── */
.usecase-panel {
    border-radius: 16px;
    padding: 1.2rem 1.4rem;
    margin: 1rem 0 1.25rem;
    background: linear-gradient(135deg, #3a4d78 0%, #344568 100%);
    border: 1px solid #5a6fa0;
    border-left: 4px solid var(--accent, #818cf8);
}
.usecase-panel h3 {
    margin: 0 0 0.35rem;
    color: #ffffff !important;
    font-size: 1.05rem;
    font-weight: 700;
}
.usecase-panel p {
    margin: 0;
    color: #cbd5e1 !important;
    font-size: 0.88rem;
    line-height: 1.55;
}

/* ── Welcome screen (Claude / Gemini style) ── */
.welcome-screen {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    min-height: 42vh;
    padding: 2rem 1.5rem 1rem;
}
.welcome-greeting {
    margin: 0 !important;
    font-size: 2.25rem !important;
    font-weight: 600 !important;
    color: #f8fafc !important;
    letter-spacing: -0.03em;
    line-height: 1.25 !important;
}
.welcome-sub {
    margin: 0.75rem 0 0 !important;
    font-size: 0.95rem !important;
    color: #94a3b8 !important;
    max-width: 420px;
}

/* Chat input zone — padded, rounded */
.chat-input-zone {
    max-width: 760px;
    margin: 0 auto;
    padding: 0 0.5rem 1.5rem;
}
div[data-testid="stChatInput"] {
    max-width: 760px;
    margin: 0 auto;
}
div[data-testid="stChatInput"] > div {
    background-color: #1e2a44 !important;
    border: 1px solid #5a6fa0 !important;
    border-radius: 16px !important;
    padding: 0.35rem 0.5rem !important;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
}
div[data-testid="stChatInput"] textarea {
    background-color: transparent !important;
    color: #f8fafc !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 14px 18px !important;
    font-size: 1rem !important;
    line-height: 1.5 !important;
    min-height: 52px !important;
}
div[data-testid="stChatInput"] textarea::placeholder {
    color: #64748b !important;
}

/* ── Section title ── */
.section-title {
    font-size: 0.78rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: #94a3b8 !important;
    margin: 1.25rem 0 0.75rem;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid #4a5d82;
}

/* ── Single conversation box (Streamlit bordered container) ── */
[data-testid="stVerticalBlockBorderWrapper"] {
    background: linear-gradient(180deg, #1e2a44 0%, #263858 100%) !important;
    border: 2px solid #5a6fa0 !important;
    border-radius: 16px !important;
    box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.06), 0 8px 24px rgba(0, 0, 0, 0.2) !important;
    padding: 0.25rem 0.5rem !important;
    min-height: 200px;
    overflow: visible !important;
}
[data-testid="stVerticalBlockBorderWrapper"] > div {
    padding: 1rem 1.15rem !important;
}

.conv-label {
    margin: 0 0 0.25rem !important;
    font-size: 0.72rem !important;
    font-weight: 700 !important;
    text-transform: uppercase;
    letter-spacing: 0.08em;
}
.conv-label-user { color: #a5b4fc !important; }
.conv-label-assistant { color: #67e8f9 !important; }
.conv-label-tool { color: #fbbf24 !important; }

.conv-divider {
    border: none;
    border-top: 1px solid #4a5d82;
    margin: 1rem 0;
    height: 0;
}

.conv-scroll-anchor {
    height: 1px;
    width: 100%;
    overflow: hidden;
    visibility: hidden;
}

[data-testid="stVerticalBlockBorderWrapper"] .stMarkdown p,
[data-testid="stVerticalBlockBorderWrapper"] .stMarkdown li {
    color: #e2e8f0 !important;
    line-height: 1.6;
}

/* ── Empty state (inside conversation box) ── */
.empty-state-inner {
    text-align: center;
    padding: 2.5rem 1rem;
}
.empty-state-inner .glow-ring {
    width: 80px;
    height: 80px;
    margin: 0 auto 1rem;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 2.2rem;
    background: linear-gradient(135deg, #4f46e5, #06b6d4);
    border: 2px solid #818cf8;
}
.empty-state-inner h3 {
    color: #ffffff !important;
    font-size: 1.15rem;
    font-weight: 700;
    margin: 0 0 0.4rem;
}
.empty-state-inner p {
    color: #94a3b8 !important;
    font-size: 0.9rem;
    max-width: 420px;
    margin: 0 auto;
}

/* ── Sidebar brand ── */
.sidebar-brand .logo-wrap {
    width: 52px;
    height: 52px;
    margin: 0 auto 0.65rem;
    border-radius: 14px;
    background: linear-gradient(135deg, #6366f1, #06b6d4);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.4rem;
    box-shadow: 0 6px 20px rgba(99, 102, 241, 0.4);
}
.sidebar-brand h2 {
    margin: 0;
    font-size: 1rem;
    font-weight: 700;
    color: #ffffff !important;
    text-align: center;
}
.sidebar-brand span {
    display: block;
    text-align: center;
    margin-top: 0.2rem;
    font-size: 0.72rem;
    color: #94a3b8 !important;
}

/* ── Status pill ── */
.status-pill {
    display: inline-block;
    padding: 0.28rem 0.7rem;
    border-radius: 999px;
    font-size: 0.72rem;
    font-weight: 700;
}
.status-pill.ready {
    background: #166534;
    color: #86efac !important;
    border: 1px solid #22c55e;
}
.status-pill.pending {
    background: #854d0e;
    color: #fde047 !important;
    border: 1px solid #eab308;
}

/* ── Loading ── */
.loading-wrap p {
    color: #cbd5e1 !important;
    text-align: center;
}
.loading-dots span {
    display: inline-block;
    width: 10px;
    height: 10px;
    margin: 0 4px;
    border-radius: 50%;
    background: #818cf8;
}

/* ── News report ── */
.news-report-wrap {
    background: #2d4068;
    border: 1px solid #5a6fa0;
    border-radius: 16px;
    padding: 1.25rem;
    margin-top: 1rem;
}

/* ── Streamlit inputs ── */
.stSelectbox > div > div,
.stTextInput > div > div > input,
div[data-testid="stChatInput"] textarea {
    background-color: #1e2a44 !important;
    color: #f8fafc !important;
    border: 1px solid #5a6fa0 !important;
    border-radius: 10px !important;
}
.stSelectbox [data-baseweb="select"] span,
.stSelectbox div[data-baseweb="select"] > div {
    background-color: #1e2a44 !important;
    color: #f8fafc !important;
}

.stButton > button {
    background-color: #334870 !important;
    color: #f8fafc !important;
    border: 1px solid #5a6fa0 !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
}
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #6366f1, #4f46e5) !important;
    color: #ffffff !important;
    border: none !important;
}

div[data-testid="stExpander"] {
    background-color: #2d4068 !important;
    border: 1px solid #4a5d82 !important;
    border-radius: 12px !important;
}
div[data-testid="stExpander"] summary,
div[data-testid="stExpander"] summary span {
    color: #f1f5f9 !important;
}

div[data-testid="stRadio"] label,
div[data-testid="stRadio"] label span,
div[data-testid="stRadio"] label p {
    color: #e2e8f0 !important;
    background-color: #2d4068 !important;
    border: 1px solid #4a5d82 !important;
    border-radius: 10px !important;
    padding: 0.5rem 0.75rem !important;
}

/* Alerts */
.stAlert > div {
    color: #1e293b !important;
}

/* Code blocks */
.stCode, pre {
    background-color: #1e2a44 !important;
    color: #e2e8f0 !important;
}

hr {
    border-color: #4a5d82 !important;
}
</style>
"""


def inject_global_styles() -> None:
    import streamlit as st

    st.markdown(GLOBAL_CSS, unsafe_allow_html=True)
