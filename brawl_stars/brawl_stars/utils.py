import json
import time

from requests import Response
from urllib.parse import urlencode
from typing import Any
from functools import partial

from .exceptions import EndpointNotFoundError, TooManyRetriesError


def _form_before_after_limit(before: str, after: str, limit: int):

    params = dict()
    if before:
        params.update({"before": before})
    if after:
        params.update({"after": after})
    if limit:
        params.update({"limit": limit})
    params = urlencode(params)
    return f"?{params}" if params else ""


class BrawlRequest:

    def __init__(self, func) -> None:
        self._func = func

    def __call__(self, *args: Any, **kwds: Any) -> Any:

        for _ in range(5):
            response: Response = self._func(*args, **kwds)
            if response.status_code in [500, 501, 502]:
                time.sleep(5)
                continue
            elif response.status_code in [404]:
                raise EndpointNotFoundError()
            break
        else:
            raise TooManyRetriesError()

        return json.loads(response.text)

    def __get__(self, instance, owner):
       return partial(self, instance)
