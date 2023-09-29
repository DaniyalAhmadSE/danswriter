class TitleNotFound(Exception):
    def __init__(self) -> None:
        super().__init__("Error: title not found!")


class HtmlDocumentNotFound(Exception):
    def __init__(self) -> None:
        super().__init__("Error: HTML document not found!")
