from typing import List
from ollama import Message as OllamaMessage, ChatResponse
from ollama import Image as OllamaImage
from pyexpat.errors import messages

from app.chat.adapter.outbound.ai.llava_repository import LlavaRepository
from app.chat.application.port.outbound.generate_chat_port import GenerateChatPort
from app.chat.domain.message import Message
from app.chat.domain.role import Role


class ChatAdapter(GenerateChatPort):
    def __init__(
            self,
            llm_repository: LlavaRepository,
    ):
        self.llm_repository = llm_repository

    def generate_chat(
            self,
            messages: List[Message]
    ) -> Message :
        ollama_message: List[OllamaMessage] = [
            OllamaMessage(
                role=message.role.value,
                content=message.content,
                images=None if message.images == [] else [
                    OllamaImage(value=image.value)
                    for image in message.images
                ]
            )
            for message in messages
        ]
        result: ChatResponse = self.llm_repository.generate_chat(ollama_message)
        return Message(
            role=Role(result.message.role),
            content=result.message.content,
            images=[]
        )
