from typing import List

class GenerateChatCommand:
    """
    메세지 생성을 위한 dto
    """
    def __init__(
            self,
            role: str,
            content: str,
            images: List[str],
    ):
        self.role = role
        self.content = content
        self.images = images
