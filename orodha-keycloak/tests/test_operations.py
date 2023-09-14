import pytest
from orodha_keycloak.connection import KeycloakConnection
from tests.fixtures.keycloak import MOCK_DATA


def test_create_user():
    connection = KeycloakConnection()
    response = connection.create_user(*MOCK_DATA.get("create_user_request"))
    assert response == MOCK_DATA.get("create_user_response")


def test_delete_user():
    connection = KeycloakConnection()
    response = connection.delete_user()
    assert response == MOCK_DATA.get("delete_user_response")
