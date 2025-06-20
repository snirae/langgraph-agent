from langchain_community.tools import DuckDuckGoSearchRun

from components.base_component import BaseComponent
from models.data_models import ToolOutput, AgentState


class WebSearch(BaseComponent):
    def __init__(self):
        self.search = DuckDuckGoSearchRun()

    def __call__(self, state: AgentState) -> dict[str, list[ToolOutput]]:
        search_result = self.search_documents(state["query"])
        output = ToolOutput(
            tool_name="web_search",
            results=[search_result],
        )
        return {"tool_outputs": [output]}

    def search_documents(self, query: str) -> str:
        return self.search.invoke(query)
