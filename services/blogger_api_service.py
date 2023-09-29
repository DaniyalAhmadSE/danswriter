import requests

from exceptions.blogger_exceptions import NoResponseError, StatusError
from services.blogger_auth_service import BloggerAuthService


class BloggerApiService:
    def __init__(
        self,
        blog_id: str,
        blogger_auth_service: BloggerAuthService,
    ) -> None:
        self.blog_id = blog_id
        self.url = f"https://www.googleapis.com/blogger/v3/blogs/{blog_id}/posts/"
        self.blogger_google_oauth_service = blogger_auth_service

    def add_post(self, title: str, content: str, labels: list[str]) -> None:
        post_data = {
            "kind": "blogger#post",
            "blog": {"id": self.blog_id},
            "title": title,
            "content": content,
            "labels": labels,
        }

        try:
            attempt_count = 0
            while attempt_count < 2:
                headers = {
                    "Authorization": self.blogger_google_oauth_service.get_token(),
                    "Content-Type": "application/json",
                }

                response = requests.post(self.url, headers=headers, json=post_data)
                if response.status_code == 200:
                    # Avoid Reattempt
                    attempt_count = 2
                    break

                # Invalid Credentials i.e. Token Expired
                if response.status_code == 401 and attempt_count < 1:
                    self.blogger_google_oauth_service.refresh_token()
                    attempt_count += 1
                else:
                    raise StatusError(response.text)

        except NoResponseError as e:
            raise e

        except StatusError as e:
            raise e
