USECASE_META = {
    "Basic Chatbot": {
        "icon": "💬",
        "tagline": "Fast conversational AI",
        "description": "Direct Groq-powered chat for Q&A, brainstorming, and coding help.",
        "accent": "#818cf8",
    },
    "Chatbot With Web": {
        "icon": "🌐",
        "tagline": "Web-grounded answers",
        "description": "ReAct agent with Tavily — searches the web when facts need to be current.",
        "accent": "#22d3ee",
    },
    "AI News": {
        "icon": "📰",
        "tagline": "Automated news digest",
        "description": "Multi-step pipeline: fetch → summarize → export a markdown report.",
        "accent": "#fb923c",
    },
}


def get_usecase_meta(usecase: str) -> dict:
    key = (usecase or "").strip()
    return USECASE_META.get(
        key,
        {
            "icon": "🤖",
            "tagline": "Agent mode",
            "description": "Select a use case in the sidebar to begin.",
            "accent": "#94a3b8",
        },
    )
