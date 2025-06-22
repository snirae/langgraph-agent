from abc import ABC

from components.base_component import BaseComponent
from llm.get_settings_prompts import get_settings_prompts
from llm.ollama_llm import Model, OllamaLLM


class BaseLLMComponent(BaseComponent, ABC):
    def __init__(
        self,
        model: Model,
        stage: str,
        stream_response: bool = False,
    ):
        self.llm = OllamaLLM(model)
        self.stage = stage
        self.settings_prompts = get_settings_prompts(stage)
        self.stream_response = stream_response
