from typing import List


from app.chat.adapter.outbound.ai.ollama_repository import OllamaRepository
from app.chat.application.port.outbound.dto.generate_chat_message import GenerateChatMessage
from app.chat.application.port.outbound.generate_chat_port import GenerateChatPort


class ChatAdapter(GenerateChatPort):
    def __init__(
            self,
            llm_repository: OllamaRepository,
    ):
        self.llm_repository = llm_repository

    def generate_chat(self, messages: List[GenerateChatMessage]) :
        message_dicts: List[dict] = [
            {
                "role": message.role,
                "content": message.content,
                "images": message.images,
            }
            for message in messages
        ]
        return self.llm_repository.generate_chat(message_dicts)
