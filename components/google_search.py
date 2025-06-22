from langchain_core.documents import Document
from langchain_google_community import GoogleSearchAPIWrapper

from components.base_component import BaseComponent
from models.data_models import AgentState


class GoogleWebSearch(BaseComponent):
    def __init__(self):
        self.search = GoogleSearchAPIWrapper()

    def __call__(self, state: AgentState) -> dict[str, list[Document]]:
        search_results = self.search_documents(state["query"])
        return {"context": search_results}

    def search_documents(self, query: str) -> list[Document]:
        result = self.search.run(query)
        results = [Document(result)]
        return results
