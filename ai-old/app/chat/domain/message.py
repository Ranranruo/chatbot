from typing import List
from app.chat.domain.role import Role
from app.core.domain.data_uri import DataURI


class Message:
    role: Role
    content: str
    images: List[str] | None = None
    def __init__(self, role: Role, content: str, images: List[str]):
        self.role = role
        self.content = content
        self.images = images