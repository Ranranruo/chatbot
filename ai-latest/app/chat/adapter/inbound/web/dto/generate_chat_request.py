from typing import Optional, List

from pydantic import BaseModel


class GenerateChatRequest(BaseModel):
    role: str
    content: str
    images: Optional[List[str]] = None