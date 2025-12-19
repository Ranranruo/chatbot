from app.chat.adapter.outbound.ai.chat_adapter import ChatAdapter
from app.chat.application.port.inbound.generate_chat_use_case import GenerateChatUseCase
from app.chat.application.service.generate_chat_service import GenerateChatService


def get_generate_chat_use_case() -> GenerateChatUseCase:
    generate_chat_port = ChatAdapter()
    return GenerateChatService(generate_chat_port)