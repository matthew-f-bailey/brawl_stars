class TooManyRetriesError(Exception):

    def __init__(self) -> None:
        self.msg = "Retries Exceeded; Cannot get response"

    def __str__(self): # pragma: no cover
        return self.msg

class EndpointNotFoundError(Exception):

    def __init__(self) -> None:
        self.msg = "Either the endpoint is typed incorrect or resource was moved"

    def __str__(self): # pragma: no cover
        return self.msg
