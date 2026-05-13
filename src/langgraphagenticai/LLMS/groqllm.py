import os

from langchain_groq import ChatGroq


class GroqLLM:
    def __init__(self, user_contols_input: dict):
        self.user_controls_input = user_contols_input or {}
        self.api_key = (self.user_controls_input.get("GROQ_API_KEY")
                        or os.getenv("GROQ_API_KEY"))
        self.model_name = self.user_controls_input.get("selected_groq_model")

    def get_llm_model(self):
        if not self.api_key:
            raise ValueError(
                "Missing GROQ API key. Set GROQ_API_KEY in the UI or environment."
            )

        if not self.model_name:
            raise ValueError(
                "Missing Groq model selection. Choose a model in the UI."
            )

        os.environ["GROQ_API_KEY"] = self.api_key

        return ChatGroq(
            model=self.model_name,
            api_key=self.api_key,
        )
