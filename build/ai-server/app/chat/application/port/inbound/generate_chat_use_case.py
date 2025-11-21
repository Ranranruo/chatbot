from abc import ABC, abstractmethod
from typing import List

from app.chat.application.port.inbound.command.generate_chat_command import GenerateChatCommand


class GenerateChatUseCase(ABC):
    @abstractmethod
    def generate_chat(self, command: GenerateChatCommand):
        """"""
        pass    
    
