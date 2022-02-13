import json

from .session import BrawlApiSession
from .utils import BrawlRequest, _form_before_after_limit


class BrawlClient:
    def __init__(self, api_key: str = None) -> None:

        self.session = BrawlApiSession()
        self.session._set_auth(api_key)

        self.host = "https://api.brawlstars.com/v1"

    @BrawlRequest
    def get_player_info(self, playerTag: str) -> list:

        playerTag = playerTag.replace("#", "%23")
        resp = self.session.get(url=f"{self.host}/players/{playerTag}")
        return resp

    @BrawlRequest
    def get_player_battlelog(self, playerTag: str) -> list:

        playerTag = playerTag.replace("#", "%23")
        resp = self.session.get(url=f"{self.host}/players/{playerTag}/battlelog")
        return resp

    @BrawlRequest
    def get_club_info(self, clubTag: str) -> list:

        clubTag = clubTag.replace("#", "%23")
        resp = self.session.get(url=f"{self.host}/clubs/{clubTag}")
        return resp

    @BrawlRequest
    def get_club_members(
        self, clubTag: str, before: str = None, after: str = None, limit: int = None
    ) -> list:

        params = _form_before_after_limit(before, after, limit)
        clubTag = clubTag.replace("#", "%23")
        resp = self.session.get(url=f"{self.host}/clubs/{clubTag}/members{params}")
        return resp

    @BrawlRequest
    def get_powerplay_seasons(
        self, countryCode: str, before: str = None, after: str = None, limit: int = None
    ) -> list:

        params = _form_before_after_limit(before, after, limit)
        resp = self.session.get(
            url=f"{self.host}/rankings/{countryCode}/powerplay/seasons{params}"
        )
        return resp

    @BrawlRequest
    def get_powerplay_season_rankings(
        self,
        countryCode: str,
        seasonId: str,
        before: str = None,
        after: str = None,
        limit: int = None,
    ) -> list:

        params = _form_before_after_limit(before, after, limit)
        resp = self.session.get(
            url=f"{self.host}/rankings/{countryCode}/powerplay/seasons/{seasonId}{params}"
        )
        return resp

    @BrawlRequest
    def get_club_rankings(
        self, countryCode: str, before: str = None, after: str = None, limit: int = None
    ) -> list:

        params = _form_before_after_limit(before, after, limit)
        resp = self.session.get(url=f"{self.host}/rankings/{countryCode}/clubs{params}")
        return resp

    @BrawlRequest
    def get_brawler_rankings(
        self,
        countryCode: str,
        brawlerId: int,
        before: str = None,
        after: str = None,
        limit: int = None,
    ) -> list:

        params = _form_before_after_limit(before, after, limit)
        resp = self.session.get(
            url=f"{self.host}/rankings/{countryCode}/brawlers/{brawlerId}{params}"
        )
        return resp

    @BrawlRequest
    def get_player_rankings(
        self, countryCode: str, before: str = None, after: str = None, limit: int = None
    ) -> list:

        params = _form_before_after_limit(before, after, limit)
        resp = self.session.get(
            url=f"{self.host}/rankings/{countryCode}/players{params}"
        )
        return resp

    @BrawlRequest
    def get_all_brawlers(
        self, before: str = None, after: str = None, limit: int = None
    ) -> list:

        params = _form_before_after_limit(before, after, limit)
        resp = self.session.get(url=f"{self.host}/brawlers{params}")
        return resp

    @BrawlRequest
    def get_brawler(
        self, brawlerId: int, before: str = None, after: str = None, limit: int = None
    ) -> list:

        resp = self.session.get(url=f"{self.host}/brawlers/{brawlerId}")
        return resp


if __name__ == "__main__":
    client = BrawlClient(
        api_key="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImNkMWNmYTM2LTllNTctNGMwYi05OWUxLTFkNDlkMjc5NzU4OSIsImlhdCI6MTY0Mzc1NjY4NCwic3ViIjoiZGV2ZWxvcGVyL2RjYjEyOGNmLWVmNDQtOWFmNC1iYjBjLTJhNzMzMWE2N2QyNiIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiNzIuNzYuNjkuMzciXSwidHlwZSI6ImNsaWVudCJ9XX0.09jBjCFlMX-fF13tCvMMqYylLdPJs67WDE8wlyUQT8K5lGac2NpVYpVkcWGRBll9UrF8IfANLDrwE8TvnSmKGQ"
    )
    # print(json.dumps(client.get_powerplay_seasons(countryCode="us"), indent=3))
    # print(json.dumps(client.get_powerplay_season_rankings(countryCode="global", seasonId="114"), indent=3))
    # print(json.dumps(client.get_club_members(clubTag="#2GU9G0282"), indent=3))
    # print(json.dumps(client.get_club_rankings(countryCode="global"), indent=3))
    # print(json.dumps(client.get_player_rankings(countryCode="global"), indent=3))
    print(json.dumps(client.get_brawler(brawlerId=16000054), indent=3))
