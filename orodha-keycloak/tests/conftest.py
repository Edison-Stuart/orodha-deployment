"""
This module contains two fixtrues which supply data to our KeycloakConnection mock in
lieu of using the python-keycloak package to connect to our server.
"""
import pytest
import unittest.mock
from fixtures import MOCKDATA

class MockKeycloakOpenIDConnection(unittest.mock.MagicMock):

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
def mock_create_admin_connection(mocker):
    mocker.patch(
        "src.orodha_keycloak.connections.create_admin_connection",
        return_value=MockKeycloakOpenIDConnection
    )
