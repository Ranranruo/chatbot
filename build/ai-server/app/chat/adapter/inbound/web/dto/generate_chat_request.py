import requests
from dataclasses import dataclass
from typing import List
from pydantic import BaseModel

from app.chat.adapter.inbound.web.dto.message_dto import MessageDTO


@dataclass
class GenerateChatRequest(BaseModel):
    messages: List[MessageDTO]