import subprocess
from constants import chatbot_constants
from exceptions.tgpt_exceptions import TgptVersionError
from services.interfaces.i_chatbot_api_service import IChatbotApiService


class TgptApiService(IChatbotApiService):
    def get_output(self, instructions: str) -> str:
        try:
            completed_process = subprocess.run(
                ["tgpt", "--whole", instructions],
                stdout=subprocess.PIPE,  # Capture the output as a byte string
                stderr=subprocess.STDOUT,
                check=True,
                text=True,  # Decode the output to a string (Python 3.5+)
            )

            # Access the captured output as a string
            captured_output = completed_process.stdout

            if chatbot_constants.VAGUE_ERROR_TEXT in captured_output:
                raise TgptVersionError()

        except subprocess.CalledProcessError as e:
            raise e

        except TgptVersionError as e:
            raise e

        return captured_output
