from typing import List

from pydantic import BaseModel


class GenerateTextResponse(BaseModel):
    response: str

