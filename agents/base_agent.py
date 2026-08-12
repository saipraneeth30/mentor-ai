from abc import ABC, abstractmethod


class BaseAgent(ABC):

    @abstractmethod
    def handle(self, message: str):
        pass