from app.chat.application.port.inbound.dto.generate_text_command import GenerateTextCommand
from app.chat.application.port.inbound.generate_text_use_case import GenerateTextUseCase
from app.chat.application.port.inbound.dto.generate_text_result import GenerateTextResult
from app.chat.application.port.outbound.generate_text_port import GenerateTextPort


class GenerateTextService(GenerateTextUseCase):
    def __init__(
            self,
            generate_text_port: GenerateTextPort
    ):
        self.generate_text_port = generate_text_port

    def execute(
            self,
            command: GenerateTextCommand
    ):
        result = self.generate_text_port.generate_text(
            command.prompt,
            command.images
        )
        return GenerateTextResult(
            response=result['response'] or ""
        )


