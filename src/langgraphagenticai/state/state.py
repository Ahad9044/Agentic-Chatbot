from typing_extensions import TypedDict, List
from langgraph.graph.message import add_messages
from typing import Annotated
from langchain_core.messages import BaseMessage


class State(TypedDict):
    """
    Represent the structure of the state used in graph
    """
    messages: Annotated[List[BaseMessage], add_messages]