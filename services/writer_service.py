import subprocess
from exceptions.tgpt_exceptions import TgptVersionError
from services.interfaces.i_chatbot_api_service import IChatbotApiService

from utilities.html_utils import HtmlUtils
from utilities.list_utils import ListUtils


class WriterService:
    def __init__(
        self,
        chatbot_api_service: IChatbotApiService,
        min_words_total: int,
        min_words_per_subheading: int,
        writer_personality: str,
        content_instructions_base: str,
        content_labels_instructions_base: str,
    ) -> None:
        self.chatbot_api_service = chatbot_api_service
        self.min_words_total = min_words_total
        self.min_words_per_subheading = min_words_per_subheading
        self.writer_personality = writer_personality
        self.content_instructions_base = content_instructions_base
        self.content_labels_instructions_base = content_labels_instructions_base

    def __get_content_instructions(self, topic: str) -> str:
        return self.content_instructions_base.format(
            writer_personality=self.writer_personality,
            topic=topic,
            min_words_total=self.min_words_total,
            min_words_per_subheading=self.min_words_per_subheading,
        )

    def __get_content_label_instructions(self, topic: str) -> str:
        return self.content_labels_instructions_base.format(topic=topic)

    def write_post_content(self, topic: str) -> str:
        try:
            output = self.chatbot_api_service.get_output(
                self.__get_content_instructions(topic),
            )
            return HtmlUtils.extract_html_document(output)
        except subprocess.CalledProcessError as e:
            raise e

        except TgptVersionError as e:
            raise e

    def create_labels(self, topic: str) -> list[str]:
        # Multiline string containing items with numbers
        return ListUtils.convert_numbered_str_to_list(
            self.chatbot_api_service.get_output(
                self.__get_content_label_instructions(topic)
            )
        )
