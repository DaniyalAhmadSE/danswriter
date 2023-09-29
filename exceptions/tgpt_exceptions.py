class TgptVersionError(Exception):
    def __init__(self) -> None:
        super().__init__("Error: tgpt version error!")
