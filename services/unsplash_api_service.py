import requests
from exceptions.unsplash_exceptions import NoImagesFoundError


class UnsplashApiService:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.base_url = "https://api.unsplash.com/search/photos"

    def search_image_url(self, query: str) -> str:
        headers = {"Authorization": f"Client-ID {self.api_key}"}
        params = {"query": query}

        try:
            response = requests.get(self.base_url, headers=headers, params=params)
            response.raise_for_status()

            data = response.json()
            if "results" in data and len(data["results"]) > 0:
                # Retrieve the URL of the first image
                image_url = data["results"][0]["urls"]["regular"]
                return image_url
            else:
                raise NoImagesFoundError()

        except requests.exceptions.RequestException as e:
            raise e
        except NoImagesFoundError as e:
            raise e
