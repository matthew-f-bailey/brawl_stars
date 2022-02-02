from brawl_stars.endpoint import Endpoint


class Players():
    def __init__(self, endpoint: Endpoint) -> None:
        self._endpoint = endpoint

    def battlelog(self, playerTag: str):
        res = self._endpoint.get("players", "battlelog", playerTag)
        print("BATTLELOG:", res)
