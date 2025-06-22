from langgraph.graph import StateGraph
from langgraph.graph.state import CompiledStateGraph

from components.llm_components.response_generator import ResponseGenerator
from components.duckduckgo_search import DuckDuckGoWebSearch
from graph.base_rag_pipeline import BaseRAGPipeline
from models.data_models import AgentState


class SimpleRAGPipeline(BaseRAGPipeline):
    @property
    def initial_state(self) -> AgentState:
        initial_state = AgentState(
            query="",
            context=[],
            answer="",
        )
        return initial_state

    def build_graph(self) -> CompiledStateGraph:
        web_search = DuckDuckGoWebSearch()
        generator = ResponseGenerator()

        graph = StateGraph(AgentState)

        graph.add_node("retrieve", web_search)
        graph.add_node("respond", generator)

        graph.set_entry_point("retrieve")
        graph.add_edge("retrieve", "respond")
        graph.set_finish_point("respond")

        return graph.compile()
