"""
This module contains two fixtrues which supply data to our KeycloakConnection mock in
lieu of using the python-keycloak package to connect to our server.
"""
import pytest
from unittest.mock import MagicMock
from unittest.mock import mo


@pytest.fixture
class MockKeycloakOpenIDConnection(MagicMock):

    def __init__(self, **kwargs):
        self.argumetns = dict(kwargs)
        super().__init__(self)

    def create_user(self):
        return {"user_data": {
                "some_data": None
                },
                "code": 200}

    def delete_user(self):
        return "user deleted"


@pytest.fixture
def mock_create_admin_connection(MockKeycloakOpenIDConnection, **kwargs):

    keycloak_connection = MockKeycloakOpenIDConnection(
        server_url=kwargs["server_user"],
        username=kwargs["username"],
        password=kwargs["password"],
        realm_name=kwargs["realm_name"],
        client_id=kwargs["client_id"],
        client_secret_key=kwargs["client_secret_key"],
        verify=True
    )

    return keycloak_connection


@pytest.fixture
def mock_keycloak_connection(mock):
    mock.patch(
        "orodha_keycloak.connection.KeycloakConnection",
        return_value=MockKeycloakConnection(**TEST_CONNECTION_ARGS)
    )
