"""Tests about homepage."""

import unittest

from muneris import create_app, read_config

from . import TEST_CONFIG


class TestHomepageAnonymous(unittest.TestCase):
    """Check homepage as anonymous user."""

    def setUp(self):
        super(TestHomepageAnonymous, self).setUp()
        self.app = create_app(read_config(TEST_CONFIG))
        self.client = self.app.test_client()

    def test_homepage_content(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 302)
        self.assertIn(b'redirect', resp.data)
        self.assertIn(b'href="/area"', resp.data)
