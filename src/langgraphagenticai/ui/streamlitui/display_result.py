import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage, BaseMessage
import json


class DisplayResultStreamlit:
    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message
        # Initialize session state for message history
        if "messages" not in st.session_state:
            st.session_state.messages = []

    def display_result_on_ui(self):
        usecase = self.usecase
        graph = self.graph
        user_message = self.user_message
        
        # Add user message to session state
        st.session_state.messages.append(HumanMessage(content=user_message))
        
        try:
            if usecase == "Basic Chatbot":
                # Prepare input with all messages
                input_state = {"messages": st.session_state.messages}
                result = graph.invoke(input_state)
                
                # Extract the last AI message from result
                if result.get("messages"):
                    for message in result["messages"]:
                        if isinstance(message, AIMessage) and message not in st.session_state.messages:
                            st.session_state.messages.append(message)
                            break
            
            elif usecase == "Chatbot With Web":
                # Prepare state and invoke the graph
                input_state = {"messages": st.session_state.messages}
                result = graph.invoke(input_state)
                
                # Add new messages to session state
                if result.get("messages"):
                    for message in result["messages"]:
                        if message not in st.session_state.messages:
                            st.session_state.messages.append(message)
            
            # Display all messages from session state
            for message in st.session_state.messages:
                if isinstance(message, HumanMessage):
                    with st.chat_message("user"):
                        st.write(message.content)
                elif isinstance(message, ToolMessage):
                    with st.chat_message("tool"):
                        st.write("🔧 Tool Output:")
                        st.write(message.content)
                elif isinstance(message, AIMessage) and message.content:
                    with st.chat_message("assistant"):
                        st.write(message.content)
        
        except Exception as e:
            st.error(f"Error processing message: {e}")
            # Remove the failed user message from session state
            if st.session_state.messages and isinstance(st.session_state.messages[-1], HumanMessage):
                st.session_state.messages.pop()