import os
import pytest
from orodha_keycloak import OrodhaKeycloakClient, OrodhaCredentials
from orodha_keycloak.exceptions import InvalidConnectionException
from tests.conftest import MockEnvironment
from tests.fixtures.keycloak import MOCK_DATA

CONNECTION_ARGS = MOCK_DATA.get("connection_args")


def test_kwarg_credentials_with_password():
    credentials = OrodhaCredentials(
        server_url=CONNECTION_ARGS["server_url"],
        realm_name=CONNECTION_ARGS["realm_name"],
        client_id=CONNECTION_ARGS["client_id"],
        password=CONNECTION_ARGS["password"],
        username=CONNECTION_ARGS["username"],
    )

    assert credentials.server_url == CONNECTION_ARGS["server_url"]
    assert credentials.realm_name == CONNECTION_ARGS["realm_name"]
    assert credentials.client_id == CONNECTION_ARGS["client_id"]
    assert credentials.username == CONNECTION_ARGS["username"]
    assert credentials.password == CONNECTION_ARGS["password"]
    assert credentials.secret_key_available is False


def test_kwarg_credentials_with_secret_key():
    credentials = OrodhaCredentials(
        server_url=CONNECTION_ARGS["server_url"],
        realm_name=CONNECTION_ARGS["realm_name"],
        client_id=CONNECTION_ARGS["client_id"],
        client_secret_key=CONNECTION_ARGS["client_secret_key"]
    )

    assert credentials.server_url == CONNECTION_ARGS["server_url"]
    assert credentials.realm_name == CONNECTION_ARGS["realm_name"]
    assert credentials.client_id == CONNECTION_ARGS["client_id"]
    assert credentials.client_secret_key == CONNECTION_ARGS["client_secret_key"]
    assert credentials.secret_key_available is True


def test_environment_credentials_with_password():
    arg_dict = {
        "server_url": CONNECTION_ARGS["server_url"],
        "realm_name": CONNECTION_ARGS["realm_name"],
        "client_id": CONNECTION_ARGS["client_id"],
        "username": CONNECTION_ARGS["username"],
        "password": CONNECTION_ARGS["password"]
    }

    with MockEnvironment(**arg_dict):
        credentials = OrodhaCredentials()

    assert credentials.server_url == CONNECTION_ARGS["server_url"]
    assert credentials.realm_name == CONNECTION_ARGS["realm_name"]
    assert credentials.client_id == CONNECTION_ARGS["client_id"]
    assert credentials.username == CONNECTION_ARGS["username"]
    assert credentials.password == CONNECTION_ARGS["password"]
    assert credentials.secret_key_available is False


def test_environment_credentials_with_secret_key():
    arg_dict = {
        "server_url": CONNECTION_ARGS["server_url"],
        "realm_name": CONNECTION_ARGS["realm_name"],
        "client_id": CONNECTION_ARGS["client_id"],
        "client_secret_key": CONNECTION_ARGS["client_secret_key"]
    }

    with MockEnvironment(**arg_dict):
        credentials = OrodhaCredentials()

    assert credentials.server_url == CONNECTION_ARGS["server_url"]
    assert credentials.realm_name == CONNECTION_ARGS["realm_name"]
    assert credentials.client_id == CONNECTION_ARGS["client_id"]
    assert credentials.client_secret_key == CONNECTION_ARGS["client_secret_key"]
    assert credentials.secret_key_available is True


def test_credentials_missing_required_args():
    with pytest.raises(InvalidConnectionException):
        OrodhaCredentials(
            client_id=CONNECTION_ARGS["client_id"],
            client_secret_key=CONNECTION_ARGS["client_secret_key"]
        )


def test_credentials_no_credential_values():
    with pytest.raises(InvalidConnectionException):
        OrodhaCredentials(
            server_url=CONNECTION_ARGS["server_url"],
            realm_name=CONNECTION_ARGS["realm_name"],
            client_id=CONNECTION_ARGS["client_id"],
        )


def test_add_user_with_secret_key(
    mock_create_admin_connection,
    mock_create_client_connection
):
    user_request_args = MOCK_DATA.get("add_user_request")

    connection = OrodhaKeycloakClient(
        server_url=CONNECTION_ARGS["server_url"],
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


def test_add_user_with_password(
    mock_create_admin_connection,
    mock_create_client_connection
):
    user_request_args = MOCK_DATA.get("add_user_request")

    connection = OrodhaKeycloakClient(
        server_url=CONNECTION_ARGS["server_url"],
        realm_name=CONNECTION_ARGS["realm_name"],
        client_id=CONNECTION_ARGS["client_id"],
        password=CONNECTION_ARGS["password"],
        username=CONNECTION_ARGS["username"],
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
    connection = OrodhaKeycloakClient(
        server_url=CONNECTION_ARGS["server_url"],
        username=CONNECTION_ARGS["username"],
        password=CONNECTION_ARGS["password"],
        realm_name=CONNECTION_ARGS["realm_name"],
        client_id=CONNECTION_ARGS["client_id"],
        client_secret_key=CONNECTION_ARGS["client_secret_key"]
    )

    response = connection.delete_user("someid")
    assert response == MOCK_DATA.get("delete_user_response")


def test_get_user_with_token(
    mock_create_client_connection,
    mock_create_admin_connection
):
    connection = OrodhaKeycloakClient(
        server_url=CONNECTION_ARGS["server_url"],
        realm_name=CONNECTION_ARGS["realm_name"],
        client_id=CONNECTION_ARGS["client_id"],
        client_secret_key=CONNECTION_ARGS["client_secret_key"]
    )
    user = connection.get_user(token={"access_token": "data"})

    assert user == MOCK_DATA["get_user_response"]


def test_get_user_with_id(
    mock_create_client_connection,
    mock_create_admin_connection
):
    connection = OrodhaKeycloakClient(
        server_url=CONNECTION_ARGS["server_url"],
        username=CONNECTION_ARGS["username"],
        password=CONNECTION_ARGS["password"],
        realm_name=CONNECTION_ARGS["realm_name"],
        client_id=CONNECTION_ARGS["client_id"],
        client_secret_key=CONNECTION_ARGS["client_secret_key"]
    )
    user = connection.get_user(user_id="someid")

    assert user == MOCK_DATA["get_user_response"]
