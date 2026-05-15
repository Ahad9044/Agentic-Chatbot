from src.langgraphagenticai.state.state import State
from langchain_core.messages import AIMessage

class ChatbotWithToolNode:
    """
    Chatbot logic enhanced with tool integration.
    """
    def __init__(self, model):
        self.llm = model

    def create_chatbot(self, tools):
        """
        Returns a chatbot node function with tool integration.
        """
        llm_with_tools = self.llm.bind_tools(tools)

        def chatbot_node(state: State):
            """
            Chatbot logic for processing the input state and returning a response.
            """
            response = llm_with_tools.invoke(state["messages"])
            # Ensure response is a proper message object
            if not isinstance(response, AIMessage):
                response = AIMessage(content=str(response))
            return {"messages": [response]}

        return chatbot_node

