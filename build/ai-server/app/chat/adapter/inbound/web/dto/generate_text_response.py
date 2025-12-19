from typing import List, Optional

from pydantic import BaseModel


class GenerateTextResponse(BaseModel):
    response: str
