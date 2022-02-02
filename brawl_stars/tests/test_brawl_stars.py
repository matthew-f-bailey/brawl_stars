#!/usr/bin/env python

"""Tests for `brawl_stars` package."""

import unittest
from unittest.mock import patch

from brawl_stars.client import BrawlClient


class TestBrawlStars(unittest.TestCase):
    """Tests for `brawl_stars` package."""

    @patch("brawl_stars.endpoint.Endpoint._load_api_key_from_env")
    def test_init_no_key(self, load_api_key_from_env):
        """Test something."""
        load_api_key_from_env.return_value = "TEST_KEY"
        client = BrawlClient()
        self.assertEqual(client._endpoint._api_key, "TEST_KEY")


class TestPlayersEndpoint(unittest.TestCase):

    @patch("brawl_stars.endpoint.Endpoint._load_api_key_from_env")
    def test_players(self, load_api_key_from_env):
        """Test something."""
        client = BrawlClient()
        client.players.battlelog()
