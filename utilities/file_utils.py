import json
from typing import Any
from builtins import open


class FileUtils:
    @staticmethod
    def write_to_text_based_file(filepath: str, content: str) -> None:
        with open(filepath, "w") as file:
            file.write(content)

    @staticmethod
    def write_json_file(filepath: str, object: Any) -> None:
        with open(filepath, "w") as outfile:
            json.dump(object, outfile, indent=4)

    @staticmethod
    def read_json_file(filepath: str) -> dict[str, Any]:
        with open(filepath, "r") as json_file:
            json_object = json.load(json_file)
        return json_object
