from langgraph.graph.state import CompiledStateGraph, StateGraph

from components.llm_components.response_generator import ResponseGenerator
from components.llm_components.sufficiency_filter import SufficiencyFilter
from components.web_search import WebSearch
from graph.base_rag_pipeline import BaseRAGPipeline
from models.data_models import AgentState


class EnhancedRAGPipeline(BaseRAGPipeline):
    @property
    def initial_state(self) -> AgentState:
        initial_state = AgentState(
            query="",
            tool_outputs=[],
            answer="",
        )
        return initial_state

    def build_graph(self) -> CompiledStateGraph:
        web_search = WebSearch()
        sufficiency_filter = SufficiencyFilter()
        generator = ResponseGenerator()

        graph = StateGraph(AgentState)

        graph.add_node("retrieve", web_search)
        graph.add_node("filter", sufficiency_filter)
        graph.add_node("respond", generator)

        graph.set_entry_point("retrieve")
        graph.add_edge("retrieve", "filter")
        graph.add_edge("filter", "respond")
        graph.set_finish_point("respond")

        return graph.compile()
