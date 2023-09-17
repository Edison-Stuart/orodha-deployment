import pytest
import orodha_keycloak.connection
from tests.fixtures.keycloak import MOCK_DATA

CONNECTION_ARGS = MOCK_DATA.get("connection_args")

def test_add_user(
        mock_create_admin_connection,
        mock_create_client_connection
    ):
    user_request_args = MOCK_DATA.get("add_user_request")

    connection = orodha_keycloak.connection.KeycloakConnection(
        server_url=CONNECTION_ARGS["server_url"],
        username=CONNECTION_ARGS["username"],
        password=CONNECTION_ARGS["password"],
        realm_name=CONNECTION_ARGS["realm_name"],
        client_id=CONNECTION_ARGS["client_id"],
        client_secret_key=CONNECTION_ARGS["client_secret_key"]
    )
    response = connection.add_user(
        email=user_request_args['email'],
        username=user_request_args['username'],
        firstName=user_request_args['firstName'],
        lastName=user_request_args['lastName'],
        password=user_request_args['credentials'][0]["value"]
    )
    assert response == MOCK_DATA.get("add_user_response")


def test_delete_user(
        mock_create_admin_connection,
        mock_create_client_connection
    ):
    connection = orodha_keycloak.connection.KeycloakConnection(
        server_url=CONNECTION_ARGS["server_url"],
        username=CONNECTION_ARGS["username"],
        password=CONNECTION_ARGS["password"],
        realm_name=CONNECTION_ARGS["realm_name"],
        client_id=CONNECTION_ARGS["client_id"],
        client_secret_key=CONNECTION_ARGS["client_secret_key"]
    )

    response = connection.delete_user("someid")
    assert response == MOCK_DATA.get("delete_user_response")

def test_check_if_user_exists_token(
        mock_create_client_connection,
        mock_create_admin_connection
    ):
    connection = orodha_keycloak.connection.KeycloakConnection(
    server_url=CONNECTION_ARGS["server_url"],
    username=CONNECTION_ARGS["username"],
    password=CONNECTION_ARGS["password"],
    realm_name=CONNECTION_ARGS["realm_name"],
    client_id=CONNECTION_ARGS["client_id"],
    client_secret_key=CONNECTION_ARGS["client_secret_key"]
    )
    user = connection.check_if_user_exists({"access_token": "data"}, is_token=True)

    assert user == MOCK_DATA["mock_decoded_token"]

def test_check_if_user_exists_user_id(
        mock_create_client_connection,
        mock_create_admin_connection
    ):
    connection = orodha_keycloak.connection.KeycloakConnection(
    server_url=CONNECTION_ARGS["server_url"],
    username=CONNECTION_ARGS["username"],
    password=CONNECTION_ARGS["password"],
    realm_name=CONNECTION_ARGS["realm_name"],
    client_id=CONNECTION_ARGS["client_id"],
    client_secret_key=CONNECTION_ARGS["client_secret_key"]
    )
    user = connection.check_if_user_exists("someid", is_token=False)

    assert user == MOCK_DATA["get_user_response"]
