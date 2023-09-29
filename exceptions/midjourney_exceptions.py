class ServerBusyError(Exception):
    def __init__(self) -> None:
        super().__init__("Error: server busy error!")
