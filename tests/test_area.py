"""Tests about homepage."""

import unittest

from muneris import create_app, read_config

from . import TEST_CONFIG


class TestAreaAnonymous(unittest.TestCase):
    """Check homepage as anonymous user."""

    def setUp(self):
        super(TestAreaAnonymous, self).setUp()
        self.app = create_app(read_config(TEST_CONFIG))
        self.client = self.app.test_client()

    def test_homepage_content(self):
        resp = self.client.get('/area')
        self.assertIn(b'Managed areas', resp.data)
