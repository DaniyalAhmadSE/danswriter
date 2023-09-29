from services.config_service import ConfigService
from services.writer_service import WriterService
from services.blogger_api_service import BloggerApiService
from services.blogger_auth_service import BloggerAuthService
from services.interfaces.i_chatbot_api_service import IChatbotApiService

from services.palm_api_service import PalmApiService
from services.tgpt_api_service import TgptApiService
from services.unsplash_api_service import UnsplashApiService
from utilities.html_utils import HtmlUtils


class App:
    def __init__(self) -> None:
        self.app_config_service: ConfigService
        self.writer_service: WriterService
        self.chatbot_api_service: IChatbotApiService
        self.picture_api_service: UnsplashApiService
        self.blogger_auth_service: BloggerAuthService
        self.blog_api_service: BloggerApiService

    def update_config(self):
        self.app_config_service = ConfigService("config.json")
        self.blogger_auth_service = BloggerAuthService(
            self.app_config_service.get_blogger_auth_setting("port"),
            self.app_config_service.get_blogger_auth_setting("token"),
            self.app_config_service.get_blogger_auth_setting("client_secrets_filepath"),
            self.app_config_service.set_blogger_auth_setting,
        )
        self.blog_api_service = BloggerApiService(
            self.app_config_service.get_blogger_setting("blog_id"),
            self.blogger_auth_service,
        )
        self.picture_api_service = UnsplashApiService(
            self.app_config_service.get_api_key("unsplash"),
        )

        engine_name = self.app_config_service.get_preference("engine")
        if engine_name == "tgpt":
            self.chatbot_api_service = TgptApiService()
        elif engine_name == "palm":
            self.chatbot_api_service = PalmApiService(
                self.app_config_service.get_api_key("palm"),
            )
        else:
            raise Exception(f"Error! {engine_name} engine has not been integrated.")

        self.writer_service = WriterService(
            self.chatbot_api_service,
            self.app_config_service.get_preference("min_words_total"),
            self.app_config_service.get_preference("min_words_per_subheading"),
            self.app_config_service.get_preference("writer_personality"),
            self.app_config_service.get_preference("content_instructions_base"),
            self.app_config_service.get_preference("content_labels_instructions_base"),
        )

    def start_app_menu(self):
        topic = input("Enter topic: ")

        print("Writing Blog...")
        content = self.writer_service.write_post_content(topic)

        labels = self.writer_service.create_labels(topic)

        print("Inserting a picture...")

        image_url = "http" + self.picture_api_service.search_image_url(topic).strip(
            "https"
        )
        content = HtmlUtils.insert_image_in_html(content, image_url, topic)

        title = HtmlUtils.extract_title(content)
        print(f"Post HTML Document:\n{content}")

        is_upload_allowed = None
        while is_upload_allowed is None:
            is_upload_allowed_str = input(
                "Do you want to continue uploading this post? (y/n): "
            )
            if is_upload_allowed_str.lower() == "y":
                is_upload_allowed = True
                print("Uploading your post...")
                self.blog_api_service.add_post(title, content, labels)
            if is_upload_allowed_str.lower() == "n":
                is_upload_allowed = False
                print("Cancelling post upload...")

        print("DONE!")

    def main(self):
        self.update_config()
        self.start_app_menu()


if __name__ == "__main__":
    app = App()
    app.main()
