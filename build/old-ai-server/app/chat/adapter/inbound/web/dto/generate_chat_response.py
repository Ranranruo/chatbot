from dataclasses import dataclass
from typing import List, Any
from pydantic import BaseModel

from app.chat.adapter.inbound.web.dto.message_dto import MessageDTO


@dataclass
class GenerateChatResponse(BaseModel):
    message: MessageDTO
