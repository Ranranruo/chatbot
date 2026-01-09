from abc import ABC, abstractmethod
from typing import List

from app.chat.domain.message import Message


class GenerateChatPort(ABC):
    """
    chat adapter의 메세지를 생성하는 메서드의 대한 추상 클래스
    """
    @abstractmethod
    def generate_chat(self, messages: List[Message]) -> Message:
        """"""
    pass
