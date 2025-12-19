from abc import ABC, abstractmethod
from typing import List

from app.chat.application.port.inbound.dto.generate_chat_command import GenerateChatCommand

from app.chat.domain.message import Message


class GenerateChatUseCase(ABC):
    @abstractmethod
    def execute(self, command: List[GenerateChatCommand]) -> Message:
        """"""
        pass