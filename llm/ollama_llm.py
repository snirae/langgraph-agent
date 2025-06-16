from enum import StrEnum
from typing import Generator

from ollama import Client


class Model(StrEnum):
    GEMMA3_1B = "gemma3:1b"
    QWEN3_06B = "qwen3:0.6b"
    GRANITE33_2B = "granite3.3:2b"


class OllamaLLM:
    def __init__(self, model: Model = Model.GEMMA3_1B):
        self.client = Client()
        self.model = str(model.value)

    def generate(
        self,
        messages: list[dict[str, str]],
        output_structure: dict = None,
    ) -> str:
        response = self.client.chat(
            model=self.model, messages=messages, format=output_structure
        )
        return response["message"]["content"]

    def generate_stream(
        self,
        messages: list[dict[str, str]],
    ) -> Generator:
        response = self.client.chat(model=self.model, messages=messages, stream=True)
        for chunk in response:
            yield chunk["message"]["content"]
