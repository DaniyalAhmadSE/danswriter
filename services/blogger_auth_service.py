from typing import Any, Callable
from google_auth_oauthlib.flow import InstalledAppFlow


class BloggerAuthService:
    def __init__(
        self,
        port: int,
        token: str,
        client_secrets_filepath: str,
        token_setter: Callable[[str, Any], None],
    ) -> None:
        self.port = port
        self.token = token
        self.client_secrets_filepath = client_secrets_filepath
        self.scopes = "https://www.googleapis.com/auth/blogger"
        self.token_setter = token_setter

    def __fetch_fresh_token(self) -> str:
        # Set up the OAuth 2.0 flow
        flow = InstalledAppFlow.from_client_secrets_file(
            self.client_secrets_filepath,
            self.scopes,
        )
        oauth_credentials = flow.run_local_server(port=self.port)

        return f"Bearer {oauth_credentials.token}"

    def get_token(self) -> str:
        return self.token

    def refresh_token(self):
        self.token = self.__fetch_fresh_token()
        self.token_setter("token", self.token)
