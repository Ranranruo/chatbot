from abc import ABC, abstractmethod
from typing import List

from app.chat.application.port.inbound.dto.generate_chat_command import GenerateChatCommand
from app.chat.application.port.inbound.dto.generate_chat_result import GenerateChatResult


class GenerateChatUseCase(ABC):
    @abstractmethod
    def execute(self, command: List[GenerateChatCommand]) -> GenerateChatResult:
        """"""
        pass