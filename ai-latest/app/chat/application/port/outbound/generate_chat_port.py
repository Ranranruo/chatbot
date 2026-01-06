from abc import ABC, abstractmethod
from typing import List

from app.chat.domain.message import Message


class GenerateChatPort(ABC):
    @abstractmethod
    def generate_chat(self, messages: List[Message]) -> Message:
        """"""
    pass
