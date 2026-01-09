class GenerateTextResult:
    """
    텍스트 생성 후 반환 dto
    """
    def __init__(
            self,
            response: str
    ):
        self.response = response