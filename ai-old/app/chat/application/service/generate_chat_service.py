from app.chat.application.port.inbound.command.generate_chat_command import GenerateChatCommand
from app.chat.application.port.inbound.generate_chat_use_case import GenerateChatUseCase
from app.chat.application.port.outbound.generate_chat_port import GenerateChatPort
from typing import List

from app.chat.domain.message import Message


class GenerateChatService(GenerateChatUseCase):
    generate_chat_port: GenerateChatPort
    def __init__(self, generate_chat_port: GenerateChatPort):
        self.generate_chat_port = generate_chat_port
    def generate_chat(self, command: GenerateChatCommand):
        messages = [Message(message.role, message.content, message.images) for message in command.messages]
        return self.generate_chat_port.generate_chat(messages)
