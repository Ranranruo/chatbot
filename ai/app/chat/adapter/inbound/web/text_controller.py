from typing import List

from fastapi import APIRouter, Depends

from app.chat.adapter.inbound.web.dto.generate_text_request import GenerateTextRequest
from app.chat.adapter.inbound.web.dto.generate_text_response import GenerateTextResponse
from app.chat.application.port.inbound.dto.generate_text_command import GenerateTextCommand
from app.chat.application.port.inbound.generate_text_use_case import GenerateTextUseCase
from app.chat.application.port.outbound.dto.generate_text_result import GenerateTextResult
from app.chat.dependency import get_generate_text_use_case

router = APIRouter(
    prefix="/text",
    tags=["text"],
)

@router.post("")
def generate_text(
        request: GenerateTextRequest,
        use_case: GenerateTextUseCase = Depends(get_generate_text_use_case),
):
    command: GenerateTextCommand = GenerateTextCommand(
        prompt=request.prompt,
        images=request.images or [],
    )

    result: GenerateTextResult = use_case.execute(command)

    return GenerateTextResponse(
        response=result.response,
    )