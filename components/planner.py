from models.data_models import Query, Plan
from llm.ollama_llm import OllamaLLM


class Planner:
    def __init__(self, llm: OllamaLLM):
        self.llm = llm

    def create_plan(self, query: Query) -> Plan:
        messages = []
        response = self.llm.generate(messages)
        steps = [step.strip() for step in response.split("\n") if step.strip()]
        return Plan(steps=steps)
