from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.documents import Document

from components.base_component import BaseComponent
from models.data_models import AgentState


class DuckDuckGoWebSearch(BaseComponent):
    def __init__(self):
        self.search = DuckDuckGoSearchRun()

    def __call__(self, state: AgentState) -> dict[str, list[Document]]:
        search_results = self.search_documents(state["query"])
        return {"context": search_results}

    def search_documents(self, query: str) -> list[Document]:
        result = self.search.invoke(query)
        results = [Document(result)]
        return results
