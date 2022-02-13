import requests
import time


class BrawlApiSession(requests.Session):

    def __init__(self, *args, **kwargs) -> None:
        super(BrawlApiSession, self).__init__(*args, **kwargs)

        self.headers.update(
            {
                "Content-Type": "application/json"
            }
        )

    def _set_auth(self, api_key: str) -> None:

        self.headers["Authorization"] = f"Bearer {api_key}"

    def get(self, *args, **kwargs):

        for _ in range(4):
            resp = super().get(*args, **kwargs)
            if resp.status_code in [500, 501]:
                time.sleep(3)
                continue
            break

        return resp
