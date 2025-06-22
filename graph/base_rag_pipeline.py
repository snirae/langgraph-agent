from abc import ABC, abstractmethod

from langgraph.graph.state import CompiledStateGraph

from models.data_models import AgentState


class BaseRAGPipeline(ABC):
    def __init__(self, stream_response: bool = False):
        self.stream_response = stream_response
        self.graph = self.build_graph()

    @property
    @abstractmethod
    def initial_state(self) -> AgentState:
        pass

    @abstractmethod
    def build_graph(self) -> CompiledStateGraph:
        pass

    def run_pipeline(self, query: str) -> AgentState:
        empty_state = self.initial_state
        empty_state["query"] = query
        result = self.graph.invoke(empty_state)
        return result
