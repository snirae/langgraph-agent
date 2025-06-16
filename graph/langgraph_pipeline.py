from langgraph.graph import StateGraph
from langgraph.graph.state import CompiledStateGraph

from models.data_models import Query
from llm.ollama_llm import OllamaLLM
from components import (
    query_rephraser,
    planner,
    tool_selector,
    tool_executor,
    tool_output_filter,
    response_generator,
)


def build_graph() -> CompiledStateGraph:
    llm = OllamaLLM()

    rephraser = query_rephraser.QueryRephraser(llm)
    answer_planner = planner.Planner(llm)
    selector = tool_selector.ToolSelector()
    executor = tool_executor.ToolExecutor()
    filterer = tool_output_filter.OutputFilter()
    generator = response_generator.ResponseGenerator(llm)

    graph = StateGraph()

    graph.add_node("rephrase", rephraser.rephrase)
    graph.add_node("plan", answer_planner.create_plan)
    graph.add_node("select", selector.select_tools)
    graph.add_node("execute", executor.execute)
    graph.add_node("filter", filterer.filter_outputs)
    graph.add_node("respond", generator.generate_response)

    graph.set_entry_point("rephrase")
    graph.add_edge("rephrase", "plan")
    graph.add_edge("plan", "select")
    graph.add_edge("select", "execute")
    graph.add_edge("execute", "filter")
    graph.add_edge("filter", "respond")

    graph.set_finish_point("respond")

    return graph.compile()


def run_pipeline(query_str: str):
    query = Query(content=query_str)
    graph = build_graph()
    result = graph.invoke({"input": query})
    return result
