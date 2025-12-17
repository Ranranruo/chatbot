from app.chat.adapter.outbound.ai.ollama_repository import OllamaRepository
from app.chat.adapter.outbound.ai.text_dapter import TextAdapter
from app.chat.application.port.inbound.generate_text_use_case import GenerateTextUseCase
from app.chat.application.port.outbound.generate_text_port import GenerateTextPort
from app.chat.application.service.generate_text_service import GenerateTextService


def get_generate_text_use_case() -> GenerateTextUseCase:
    return GenerateTextService(
        generate_text_port=get_generate_text_port()
    )

def get_generate_text_port() -> GenerateTextPort:
    return TextAdapter(
        llm_repository=get_llm_repository()
    )

def get_llm_repository() -> OllamaRepository:
    return OllamaRepository()