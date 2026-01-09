from typing import List

class GenerateTextCommand:
    """
    단순 텍스트 생성을 위한 dto
    """
    def __init__(
            self,
            prompt: str,
            images: List[str],
    ):
        self.prompt = prompt
        self.images = images
