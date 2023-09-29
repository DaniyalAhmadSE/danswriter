from html.parser import HTMLParser
import re

from exceptions.chatbot_exceptions import HtmlDocumentNotFound, TitleNotFound


class TitleParser(HTMLParser):
    def __init__(self, html_string: str):
        super().__init__()
        self.in_title = False
        self.__title = ""
        self.feed(html_string)

    def handle_starttag(self, tag: str, attrs):
        if tag == "title":
            self.in_title = True

    def handle_data(self, data):
        if self.in_title:
            self.__title += data

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    @property
    def title(self):
        return self.__title.strip()


class ImgInserter(HTMLParser):
    def __init__(self, html_string, image_url, alt_text):
        super().__init__()
        self.modified_html = ""
        self.img_inserted = False
        self.image_url = image_url
        self.alt_text = alt_text
        self.feed(html_string)

    def handle_starttag(self, tag, attrs):
        self.modified_html += f"<{tag}"
        for attr in attrs:
            self.modified_html += f' {attr[0]}="{attr[1]}"'
        self.modified_html += ">"

    def handle_endtag(self, tag):
        self.modified_html += f"</{tag}>"
        if tag == "p" and not self.img_inserted:
            # Insert the <img> element here
            self.modified_html += f'<img src="{self.image_url}" alt="{self.alt_text}">'
            self.img_inserted = True

    def handle_data(self, data):
        self.modified_html += data


class HtmlUtils:
    @staticmethod
    def extract_title(html_string: str) -> str:
        parser = TitleParser(html_string)
        title = parser.title
        if title:
            return title
        else:
            raise TitleNotFound()

    @staticmethod
    def insert_image_in_html(html_string: str, image_url: str, alt_text: str) -> str:
        parser = ImgInserter(html_string, image_url, alt_text)
        return parser.modified_html

    @staticmethod
    def extract_html_document(input_string: str) -> str:
        # Define a regular expression pattern to match the HTML document
        html_pattern = r"<html[\s\S]*?</html>"

        # Use re.DOTALL to match across multiple lines
        html_match = re.search(html_pattern, input_string, re.DOTALL)

        if html_match:
            # Extract the matched HTML document
            html_document = html_match.group()
            return html_document
        else:
            raise HtmlDocumentNotFound()
