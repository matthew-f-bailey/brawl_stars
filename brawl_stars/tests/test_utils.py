import unittest
from unittest.mock import MagicMock, patch

from brawl_stars.brawl_stars.utils import _form_before_after_limit, BrawlRequest
from brawl_stars.brawl_stars.exceptions import TooManyRetriesError, EndpointNotFoundError

class TestBeforeAfterLimit(unittest.TestCase):

    def test_all_cases(self):

        self.assertEqual(
            _form_before_after_limit("123", None, None),
            "?before=123"
        )
        self.assertEqual(
            _form_before_after_limit("123", "after", None),
            "?before=123&after=after"
        )
        self.assertEqual(
            _form_before_after_limit("123", "654", 5),
            "?before=123&after=654&limit=5"
        )

class TestBrawlRequestDecorator(unittest.TestCase):

    def setUp(self) -> None:

        class InnerClass:

            @BrawlRequest
            def test_retry_method(self):
                mock = MagicMock()
                mock.status_code = 500
                return mock

            @BrawlRequest
            def test_404(self):
                mock = MagicMock()
                mock.status_code = 404
                return mock

            @BrawlRequest
            def test_valid(self):
                mock = MagicMock()
                mock.status_code = 200
                mock.text = '{"foo":"bar"}'
                return mock

        self.cls = InnerClass()

    @patch("brawl_stars.brawl_stars.utils.time", return_value=None)
    def test_too_many_retries(self, mock_sleep):

        with self.assertRaises(TooManyRetriesError):
            self.cls.test_retry_method()

    def test_404(self):

        with self.assertRaises(EndpointNotFoundError):
            self.cls.test_404()

    def test_valid(self):

        self.assertEqual(
            self.cls.test_valid(),
            {"foo":"bar"}
        )
