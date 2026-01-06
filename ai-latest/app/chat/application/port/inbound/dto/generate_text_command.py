from typing import List

class GenerateTextCommand:
    def __init__(
            self,
            prompt: str,
            images: List[str],
    ):
        self.prompt = prompt
        self.images = images
