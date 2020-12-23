"""Module to define authentication tests."""
from django.test import TestCase
from rest_framework_simplejwt.models import TokenUser
from rest_framework_simplejwt.settings import api_settings

AuthToken = api_settings.AUTH_TOKEN_CLASSES[0]


class TodoTest(TestCase):
    """Test definitions for Auth Models."""

    def setUp(self):
        """Setups definition for Auth Models."""
        self.token = AuthToken()
        self.token[api_settings.USER_ID_CLAIM] = 33
        self.token["username"] = "daron"
        self.token["first_name"] = "Daron"
        self.token["last_name"] = "Malakian"
        self.token["email"] = "daron@soad.com"

        self.user = TokenUser(self.token)

    # test for tokens
    def test_username(self):
        """Validates that username exists."""
        self.assertEqual(self.user.username, "daron")
