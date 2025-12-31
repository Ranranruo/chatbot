from abc import ABC, abstractmethod
import ollama
from typing import List

from ollama import Message

class LLMRepository:
    def generate_chat(self, messages):
        result = ollama.chat(
            model="llava:7b",
            messages=messages
        )
        return result
