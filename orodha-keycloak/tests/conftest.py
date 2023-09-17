"""
This module contains two fixtrues which supply our mock admin connections to
our KeycloakConnection in lieu of using the python-keycloak package to connect to our server.
"""
from unittest.mock import MagicMock
import pytest
from tests.fixtures.keycloak import MOCK_DATA


class MockKeycloakAdmin(MagicMock):
    """Mocked Admin KeycloakOpenIdConnection object used to mock admin
        keycloak functions in testing."""
    def __init__(self, **kwargs):
        self.argumetns = dict(kwargs)
        super().__init__(self)

    def create_user(self, **kwargs):
        return MOCK_DATA["add_user_response"]

    def delete_user(user_id=None):
        return MOCK_DATA.get("delete_user_response")

    def get_user(user_id=None):
        return MOCK_DATA.get("get_user_response")

class MockKeycloakClient(MagicMock):
    """Mocked Client KeycloakOpenId object used to mock client keycloak functions in testing."""
    def __init__(self, **kwargs):
        super().__init__(self)

    def public_key():
        return MOCK_DATA["mock_public_key"]

    def decode_token(token, key={}, options={}):
        return MOCK_DATA.get("mock_decoded_token")


@pytest.fixture
def mock_create_client_connection(mocker):
    """
    Fixture which patches our create_client_connection function to return our mocked client.
    """
    mocker.patch(
        "orodha_keycloak.connections.client.create_client_connection",
        return_value=MockKeycloakClient,
    )

@pytest.fixture
def mock_create_admin_connection(mocker):
    """
    Fixture which patches our create_admin_connection function to return our mocked client.
    """
    mocker.patch(
        "orodha_keycloak.connections.admin.create_admin_connection",
        return_value=MockKeycloakAdmin,
    )
