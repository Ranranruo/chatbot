from typing import List

from app.chat.domain.image import Image
from app.chat.domain.role import Role


class Message:
    role: Role
    content: str
    images: List[Image]

    def __init__(
            self,
            role: Role,
            content: str,
            images: List[Image]
    ):
        self.role = role
        self.content = content
        self.images = images