from abc import ABC, abstractmethod
from typing import List


class GenerateTextPort(ABC):
    @abstractmethod
    def generate_text(self, prompt: str, images: List[str]):
        """"""
    pass
