import streamlit as st

from langchain_core.messages import HumanMessage


class DisplayResultStreamlit:
    def __init__(self, usecase: str, graph, user_message: str):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display_result_on_ui(self):
        if not self.graph:
            st.error("Error: Graph not initialized.")
            return

        if not self.user_message:
            st.error("Error: No user message provided.")
            return

        with st.spinner("Generating response..."):
            try:
                result = self.graph.invoke({"messages": [HumanMessage(content=self.user_message)]})
                response_text = result["messages"][-1].content

                if not response_text:
                    st.error("Error: Response generation returned empty text.")
                    return

                st.markdown("**Response:**")
                st.write(response_text)

            except Exception as e:
                st.error(f"Error generating response: {e}")
                st.write(response_text)
            except Exception as exc:
                st.error(f"Error generating response: {exc}")
