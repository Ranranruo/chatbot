from typing import List

from app.chat.adapter.outbound.ai.llm_repository import LLMRepository
from app.chat.application.port.outbound.generate_chat_port import GenerateChatPort
from app.chat.domain.message import Message


class ChatAdapter(GenerateChatPort):

    def generate_chat(self, messages: List[Message]) -> List[Message]:
        repo = LLMRepository()
        requestMessages = []

        for message in messages:
            temp = {
                "role": message.role,
                "content": message.content,
            }

            # images가 있을 때만 넣기
            if message.images:
                temp["images"] = message.images  # base64 문자열 그대로

            requestMessages.append(temp)

        return repo.generate_chat(requestMessages)

