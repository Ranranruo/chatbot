from typing import List

import ollama
from ollama import Message as OllamaMessage
from app.chat.domain.message import Message


class OllamaRepository:
    def generate_text(self, prompt: str, images: List[str]):
        result = ollama.generate(
            model="llava:7b",
            prompt=prompt,
            images=images,
        )
        return result

    def generate_chat(self, messages: List[OllamaMessage]):
        result = ollama.chat(
            model="llava:7b",
            messages=messages
        )
        return result