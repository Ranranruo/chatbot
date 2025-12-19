from fastapi import APIRouter, Depends, UploadFile, File, Form
import os

from app.chat.adapter.inbound.web.dto.generate_chat_response import GenerateChatResponse
from app.chat.adapter.inbound.web.dto.message_dto import MessageDTO
from app.chat.application.port.inbound.command.generate_chat_command import GenerateChatCommand
from app.chat.application.port.inbound.generate_chat_use_case import GenerateChatUseCase
from app.chat.adapter.inbound.web.dto.generate_chat_request import GenerateChatRequest
from typing import List

from app.chat.dependency import get_generate_chat_use_case
from app.chat.domain.message import Message

router = APIRouter(
    prefix="/chat",
    tags=["chat"]
)

@router.post("")
def generate_chat(request: List[MessageDTO], generate_chat_use_case: GenerateChatUseCase = Depends(get_generate_chat_use_case)) -> GenerateChatResponse:
    messages = [Message(chatRequest.role, chatRequest.content, chatRequest.images) for chatRequest in request]
    for message in messages:
        for image in message.images:
            if image == "":
                message.images.remove(image)

    result = generate_chat_use_case.generate_chat(GenerateChatCommand(messages))
    return result
