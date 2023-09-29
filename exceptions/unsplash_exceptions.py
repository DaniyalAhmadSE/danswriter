class NoImagesFoundError(Exception):
    def __init__(self) -> None:
        super().__init__("Error: no images found!")
