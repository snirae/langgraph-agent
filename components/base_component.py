from abc import ABC, abstractmethod

from models.data_models import AgentState


class BaseComponent(ABC):
    @abstractmethod
    def __call__(self, state: AgentState):
        raise NotImplementedError
