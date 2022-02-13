import unittest

from unittest.mock import MagicMock, patch

from brawl_stars.brawl_stars.exceptions import (
    TooManyRetriesError, EndpointNotFoundError)

class TestBeforeAfterLimit(unittest.TestCase):

    def test_exceptions_are_exceptions(self):

        exc = TooManyRetriesError()
        self.assertIsInstance(
            exc.msg,
            str
        )
        exc = EndpointNotFoundError()
        self.assertIsInstance(
            exc.msg,
            str
        )
