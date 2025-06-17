from langgraph.graph import StateGraph
from langgraph.graph.state import CompiledStateGraph

from components.llm_components.response_generator import ResponseGenerator
from components.tool_output_filter import OutputFilter
from components.web_search import WebSearch
from models.data_models import AgentState


def build_graph() -> CompiledStateGraph:
    web_search = WebSearch()
    results_filter = OutputFilter()
    generator = ResponseGenerator()

    graph = StateGraph(AgentState)

    graph.add_node("retrieve", web_search)
    graph.add_node("results_filter", results_filter)
    graph.add_node("respond", generator)

    graph.set_entry_point("retrieve")

    graph.add_edge("retrieve", "results_filter")
    graph.add_edge("results_filter", "respond")

    graph.set_finish_point("respond")

    return graph.compile()


def run_pipeline(query: str) -> AgentState:
    empty_state = AgentState(
        query=query,
        tool_outputs=[],
        answer="",
    )
    graph = build_graph()
    result = graph.invoke(empty_state)
    return result
