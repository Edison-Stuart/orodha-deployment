"""
This module contains two fixtrues which supply our mock  admin connection to
our KeycloakConnection in lieu of using the python-keycloak package to connect to our server.
"""
from unittest.mock import MagicMock
import pytest
from tests.fixtures.keycloak import MOCK_DATA


class MockKeycloakAdmin(MagicMock):
    def __init__(self, **kwargs):
        self.argumetns = dict(kwargs)
        super().__init__(self)

    def create_user(self):
        return MOCK_DATA.get("create_user_response")

    def delete_user(self):
        return MOCK_DATA.get("delete_user_response")


@pytest.fixture
def mock_create_admin_connection(mocker):
    mocker.patch(
        "src.orodha_keycloak.connections.create_admin_connection",
        return_value=MockKeycloakAdmin,
    )
