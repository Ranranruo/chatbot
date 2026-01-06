from typing import List, Optional

from pydantic import BaseModel


class GenerateTextRequest(BaseModel):
    prompt: str
    images: Optional[List[str]] = None
