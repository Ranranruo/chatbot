from typing import Optional, List

from pydantic import BaseModel


class GenerateChatResponse(BaseModel):
    role: str
    content: str