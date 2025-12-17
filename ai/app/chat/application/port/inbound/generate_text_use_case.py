from abc import ABC, abstractmethod
from typing import List

from app.chat.application.port.inbound.dto.generate_text_command import GenerateTextCommand
from app.chat.application.port.outbound.dto.generate_text_result import GenerateTextResult


class GenerateTextUseCase(ABC):
    @abstractmethod
    def execute(self, command: GenerateTextCommand) -> GenerateTextResult:
        """"""
        pass