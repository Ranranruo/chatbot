from typing import List

from app.chat.application.port.inbound.dto.generate_chat_command import GenerateChatCommand
from app.chat.application.port.inbound.dto.generate_text_command import GenerateTextCommand
from app.chat.application.port.inbound.generate_chat_use_case import GenerateChatUseCase
from app.chat.application.port.inbound.dto.generate_text_result import GenerateTextResult
from app.chat.application.port.outbound.dto.generate_chat_message import GenerateChatMessage
from app.chat.application.port.outbound.generate_chat_port import GenerateChatPort
from app.chat.domain.image import Image
from app.chat.domain.message import Message
from app.chat.domain.role import Role


class GenerateChatService(GenerateChatUseCase):
    """
    메세지 생성 비지니스 로직
    """
    def __init__(
            self,
            generate_chat_port: GenerateChatPort,
    ):
        self.generate_chat_port = generate_chat_port
    def execute(self, command: List[GenerateChatCommand]) -> Message:
        # command 데이터 -> Message(Domain)배열로 변환
        messages: List[Message] = [
            Message(
                role=Role(message.role),
                content=message.content,
                images=[
                    Image(image)
                    for image in message.images
                    if image  # 빈 문자열, None 전부 제거
                ] if message.images else None  # 아예 없으면 None
            )
            for message in command
        ]
        result = self.generate_chat_port.generate_chat(messages)

        # 결과 반환
        return Message(
            role=result.role,
            content=result.content,
            images=[]
        )