from abc import ABC, abstractmethod
from typing import TypedDict

from langgraph.graph.state import CompiledStateGraph

from models.data_models import AgentState


class BaseRAGPipeline(ABC):
    def __init__(self):
        self.graph = self.build_graph()

    @property
    @abstractmethod
    def initial_state(self) -> AgentState:
        pass

    @abstractmethod
    def build_graph(self) -> CompiledStateGraph:
        pass

    def run_pipeline(self, query: str) -> TypedDict:
        empty_state = self.initial_state
        empty_state["query"] = query
        result = self.graph.invoke(empty_state)
        return result
