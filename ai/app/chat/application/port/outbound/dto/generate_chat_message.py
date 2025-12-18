from typing import List


class GenerateChatMessage:
    role: str
    content: str
    images: List[str]
    def __init__(
            self,
            role,
            content,
            images,
    ):
        self.role = role
        self.content = content
        self.images = images
