from abc import ABC, abstractmethod

from app.chat.application.port.inbound.dto.generate_text_command import GenerateTextCommand
from app.chat.application.port.inbound.dto.generate_text_result import GenerateTextResult


class GenerateTextUseCase(ABC):
    """
    단순 텍스트 생성 Service 추상 클래스
    """
    @abstractmethod
    def execute(self, command: GenerateTextCommand) -> GenerateTextResult:
        """"""
        pass