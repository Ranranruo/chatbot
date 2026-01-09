from abc import ABC, abstractmethod
from typing import List


class GenerateTextPort(ABC):
    """
    text adapter의 단순 텍스트를 생성하는 메서드의 대한 추상 클래스
    """
    @abstractmethod
    def generate_text(self, prompt: str, images: List[str]):
        """"""
    pass
