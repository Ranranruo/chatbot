from typing import List
from wsgiref.util import request_uri

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

@router.post(
    "",
    summary="텍스트 생성",
    description="프롬포트와 이미지를 기반으로 AI 텍스트를 생성한다.",
    response_model=GenerateTextResponse,
)
def generate_text(
        request: GenerateTextRequest,
        use_case: GenerateTextUseCase = Depends(get_generate_text_use_case),
):
    # service
    command: GenerateTextCommand = GenerateTextCommand(
        prompt=request.prompt,
        images=request.images or [],
    )

    result: GenerateTextResult = use_case.execute(command)

    return GenerateTextResponse(
        response=result.response,
    )