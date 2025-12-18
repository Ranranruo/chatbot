from typing import List

from app.chat.application.port.inbound.dto.generate_chat_command import GenerateChatCommand
from app.chat.application.port.inbound.dto.generate_chat_result import GenerateChatResult
from app.chat.application.port.inbound.dto.generate_text_command import GenerateTextCommand
from app.chat.application.port.inbound.generate_chat_use_case import GenerateChatUseCase
from app.chat.application.port.inbound.dto.generate_text_result import GenerateTextResult
from app.chat.application.port.outbound.dto.generate_chat_message import GenerateChatMessage
from app.chat.application.port.outbound.generate_chat_port import GenerateChatPort
from app.chat.domain.message import Message
from app.chat.domain.role import Role


class GenerateChatService(GenerateChatUseCase):
    def __init__(
            self,
            generate_chat_port: GenerateChatPort,
    ):
        self.generate_chat_port = generate_chat_port
    def execute(self, command: List[GenerateChatCommand]) -> Message:
        generate_chat_messages: List[GenerateChatMessage] = [
            GenerateChatMessage(
                role=message.role,
                content=message.content,
                images=message.images
            )
            for message in command
        ]
        result = self.generate_chat_port.generate_chat(generate_chat_messages)

        return Message(
            role=Role.ASSISTANT,
            content=result.message.content,
            images=[]
        )