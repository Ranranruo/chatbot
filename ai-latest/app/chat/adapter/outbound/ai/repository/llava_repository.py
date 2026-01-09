from typing import List

import os
from ollama import Message as OllamaMessage
from ollama import Client
from app.chat.domain.message import Message

# 환경 변수에서 ollama서버 주소를 읽어오며 기본값은 "http://localhost:11434"로 설정한다.
OLLAMA_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

# 읽어온 ollama서버의 주소를 설정한다.
ollama = Client(host=OLLAMA_URL)

class LlavaRepository:
    def generate_text(self, prompt: str, images: List[str]):
        """
        텍스트를 생성한다.
        """
        result = ollama.generate(
            model="llava:7b",
            prompt=prompt,
            images=images,
        )
        return result

    def generate_chat(self, messages: List[OllamaMessage]):
        """
        대화를 생성한다.
        """
        result = ollama.chat(
            model="llava:7b",
            messages=messages
        )
        return result