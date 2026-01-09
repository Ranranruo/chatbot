from typing import List


class GenerateChatMessage:
    """
    chat adapter에 메세지를 생성하는 메서드의 인자 dto
    """
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
