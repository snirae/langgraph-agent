from copy import deepcopy
from functools import partial

from langchain_core.documents import Document

from components.base_component import BaseComponent
from models.data_models import AgentState


class ContextReorder(BaseComponent):
    def __call__(self, state: AgentState) -> dict[str, list[Document]]:
        reordered_documents = self.reorder_documents(state["context"])
        return {"context": reordered_documents}

    def reorder_documents(self, documents: list[Document]) -> list[Document]:
        k = len(documents)
        reordered_documents = deepcopy(documents)
        relocate = partial(self._relocate_document, k=k)
        for i, document in enumerate(documents, start=1):
            new_location = relocate(i) - 1
            reordered_documents[new_location] = document
        return reordered_documents

    @staticmethod
    def _relocate_document(idx: int, k: int) -> int:
        if idx % 2 == 0:
            return (k + 1) - int((idx / 2))
        else:
            return int((idx + 1) / 2)
