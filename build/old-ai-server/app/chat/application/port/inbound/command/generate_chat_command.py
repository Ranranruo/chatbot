import dataclasses

from app.chat.domain.message import Message

@dataclasses.dataclass
class GenerateChatCommand:
    messages: list[Message]