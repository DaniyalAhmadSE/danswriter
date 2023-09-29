from abc import ABC, abstractmethod


class IChatbotApiService(ABC):
    @abstractmethod
    def get_output(self, instructions: str) -> str:
        pass
