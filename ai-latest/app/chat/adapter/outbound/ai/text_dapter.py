from typing import List


from app.chat.adapter.outbound.ai.llava_repository import LlavaRepository
from app.chat.application.port.outbound.generate_text_port import GenerateTextPort


class TextAdapter(GenerateTextPort):
    def __init__(
            self,
            llm_repository: LlavaRepository,
    ):
        self.llm_repository = llm_repository
    def generate_text(self, prompt: str, images: List[str]):
        return self.llm_repository.generate_text(prompt, images)

