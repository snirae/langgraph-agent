from llm.ollama_llm import OllamaLLM
from models.data_models import Query


class QueryRephraser:
    def __init__(self, llm: OllamaLLM):
        self.llm = llm

    def rephrase(self, query: Query) -> Query:
        messages = []
        response = self.llm.generate(messages)
        return Query(content=response)
