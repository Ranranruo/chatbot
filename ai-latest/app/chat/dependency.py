from app.chat.adapter.outbound.ai.chat_dapter import ChatAdapter
from app.chat.adapter.outbound.ai.repository.llava_repository import LlavaRepository
from app.chat.adapter.outbound.ai.text_dapter import TextAdapter
from app.chat.application.port.inbound.generate_chat_use_case import GenerateChatUseCase
from app.chat.application.port.inbound.generate_text_use_case import GenerateTextUseCase
from app.chat.application.port.outbound.generate_chat_port import GenerateChatPort
from app.chat.application.port.outbound.generate_text_port import GenerateTextPort
from app.chat.application.service.generate_chat_service import GenerateChatService
from app.chat.application.service.generate_text_service import GenerateTextService

"""
의존성 관리
"""

def get_generate_text_use_case() -> GenerateTextUseCase:
    return GenerateTextService(
        generate_text_port=get_generate_text_port()
    )

def get_generate_text_port() -> GenerateTextPort:
    return TextAdapter(
        llm_repository=get_llm_repository()
    )

def get_generate_chat_use_case() -> GenerateChatUseCase:
    return GenerateChatService(
        generate_chat_port=get_generate_chat_port()
    )

def get_generate_chat_port() -> GenerateChatPort:
    return ChatAdapter(
        llm_repository=get_llm_repository()
    )

def get_llm_repository() -> LlavaRepository:
    return LlavaRepository()