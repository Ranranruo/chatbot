from typing import List

class GenerateChatCommand:
    def __init__(
            self,
            role: str,
            content: str,
            images: List[str],
    ):
        self.role = role
        self.content = content
        self.images = images
