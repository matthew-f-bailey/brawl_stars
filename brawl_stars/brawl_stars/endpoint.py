import requests
import json

from dotenv import dotenv_values


class Endpoint:

    def __init__(self, api_key: str) -> None:
        self._api_key = api_key
        if not api_key:
            self._api_key = self._load_api_key_from_env()

        self._headers = {
            "authorization": f"Bearer {self._api_key}"
        }

    def get(self, point: str, action: str, *args):

        args = '/'.join(args)
        url = f"https://api.brawlstars.com/v1/{point}/%23L2V2LR8Q/{action}"
        print(f"Getting info @ Url: {url}\nAnd API_KEY: {self._api_key}")
        res = requests.get(
            url=url,
            headers={"authorization": f"Bearer {self._api_key}"}
        )
        print(res.status_code)
        return res.text

    def _load_api_key_from_env(self):
        """Load in api key from env file
        See https://pypi.org/project/python-dotenv/
        """
        config = dotenv_values()
        try:
            api_key = config["API_KEY"]
        except KeyError:
            raise KeyError("Could not load in API_KEY property from .env")

        return api_key
