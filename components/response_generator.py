from typing import List
from models.data_models import ToolOutput
from llm.ollama_llm import OllamaLLM


class ResponseGenerator:
    def __init__(self, llm: OllamaLLM):
        self.llm = llm

    def generate_response(self, outputs: List[ToolOutput]) -> str:
        combined_results = "\n".join(output.result for output in outputs)
        prompt = f"Summarize the following results into a helpful response:\n\n{combined_results}"
        return self.llm.chat(prompt)
