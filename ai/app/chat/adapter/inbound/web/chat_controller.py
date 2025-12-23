from typing import List

from fastapi import APIRouter, Depends

from app.chat.adapter.inbound.web.dto.generate_chat_request import GenerateChatRequest
from app.chat.adapter.inbound.web.dto.generate_chat_response import GenerateChatResponse
from app.chat.application.port.inbound.dto.generate_chat_command import GenerateChatCommand
from app.chat.application.port.inbound.generate_chat_use_case import GenerateChatUseCase
from app.chat.dependency import get_generate_chat_use_case
from app.chat.domain.message import Message

router = APIRouter(
    prefix="/chat",
    tags=["chat"],
)
@router.post(
    "",
    summary="메세지 생성",
    description="메세지 객체 배열을 받아 새로운 메세지를 생성합니다.",
    response_model=GenerateChatResponse,
)
def generate_chat(
        messages: List[GenerateChatRequest],
        use_case: GenerateChatUseCase = Depends(get_generate_chat_use_case)
):
    command: List[GenerateChatCommand] = []

    for message in messages:
        images: List[str] = []
        for image in message.images:
            images.append(image)

        command.append(GenerateChatCommand(
            role=message.role,
            content=message.content,
            images=images,
        ))

    result: Message = use_case.execute(command)

    return GenerateChatResponse(
        role=result.role.value,
        content=result.content,
    )