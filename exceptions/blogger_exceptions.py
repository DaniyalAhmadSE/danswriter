class NoResponseError(Exception):
    def __init__(self) -> None:
        super().__init__("Error: no response!")


class StatusError(Exception):
    def __init__(self, message) -> None:
        super().__init__(f"Status Error: {message}")
