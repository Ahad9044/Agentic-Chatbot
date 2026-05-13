import streamlit as st

from langchain_core.messages import HumanMessage


class DisplayResultStreamlit:
    def __init__(self, usecase: str, graph: dict, user_message: str):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def _extract_response_text(self, result):
        if not result or not getattr(result, "generations", None):
            return ""

        batch = result.generations[0]
        if not batch:
            return ""

        generation = batch[0]
        if hasattr(generation, "text") and generation.text:
            return generation.text

        message = getattr(generation, "message", None)
        if message is not None:
            return getattr(message, "content", str(message))

        return str(generation)

    def display_result_on_ui(self):
        model = self.graph.get("model") if isinstance(self.graph, dict) else getattr(self.graph, "model", None)

        if not model:
            st.error("Error: No model found to generate the response.")
            return

        if not self.user_message:
            st.error("Error: No user message provided.")
            return

        with st.spinner("Generating response..."):
            try:
                result = model.generate([[HumanMessage(content=self.user_message)]])
                response_text = self._extract_response_text(result)

                if not response_text:
                    st.error("Error: Response generation returned empty text.")
                    return

                st.markdown("**Response:**")
                st.write(response_text)
            except Exception as exc:
                st.error(f"Error generating response: {exc}")
