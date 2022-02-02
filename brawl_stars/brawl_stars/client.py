from brawl_stars.endpoint import Endpoint
from brawl_stars.players import Players#, clubs, rankings, brawlers, events


class BrawlClient:

    def __init__(self, api_key: str = None) -> None:

        # Take API key from init or get via .env
        self._endpoint = Endpoint(api_key)

        #Compose Client of endpoints
        self.players = Players(self._endpoint)
        # self.clubs = clubs.Clubs(self._endpoint)
        # self.rankings = rankings.Rankings(self._endpoint)
        # self.brawlers = brawlers.Brawlers(self._endpoint)
        # self.events = events.Events(self._endpoint)

if __name__=="__main__":
    client = BrawlClient()
    client.players.battlelog("#L2V2LR8Q")
