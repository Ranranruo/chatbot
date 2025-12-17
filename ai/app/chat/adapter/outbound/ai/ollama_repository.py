from typing import List

import ollama

class OllamaRepository:
    def generate_text(self, prompt: str, images: List[str]):
        result = ollama.generate(
            model="llava:7b",
            prompt=prompt,
            images=images,
        )
        return result