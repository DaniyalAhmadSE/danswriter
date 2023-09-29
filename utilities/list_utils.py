import re


class ListUtils:
    @staticmethod
    def convert_numbered_str_to_list(numbered_string: str) -> list[str]:
        return re.findall(r"\d+\.\s+(.*)", numbered_string)
