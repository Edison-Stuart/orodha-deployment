"""
This Module contains a function which provides a keycloak connection
set up as an admin for our main class.
"""
from keycloak import KeycloakAdmin, KeycloakOpenIDConnection
from orodha_keycloak.connections.exceptions import InvalidConnectionException

ADMIN_ARG_LIST = [
    "server_url",
    "username",
    "password",
    "realm_name",
    "client_id",
    "client_secret_key",
]


def create_admin_connection(**kwargs):
    """
    Creates and returns keycloak admin connection with given args

    Args:
        server_user: User that has admin priveleges on the server.
        username: The username of the server_user.
        password: The password of the server_user.
        realm_name: The name of the keycloak realm that we are attempting to access.
        client_id: The keycloak client_id that we are using for the connection.
        client_secret_key: The secret key of the keycloak client.

    Raises:
        InvalidConnectionException: If the connection arguments are missing and the connection will
            be unable to complete

    Returns:
        keycloak_admin: This object is what holds our connection to the keycloak admin, through this
            we are able to manipulate users and other data depending on the keycloak permissions.
    """
    if list(kwargs.keys()) != ADMIN_ARG_LIST:
        missing_args = [arg for arg in ADMIN_ARG_LIST if arg not in list(kwargs.keys())]
        raise InvalidConnectionException(missing_args=missing_args)

    keycloak_connection = KeycloakOpenIDConnection(
        server_url=kwargs.get("server_user"),
        username=kwargs.get("username"),
        password=kwargs.get("password"),
        realm_name=kwargs.get("realm_name"),
        client_id=kwargs.get("client_id"),
        client_secret_key=kwargs.get("client_secret_key"),
        verify=True,
    )
    keycloak_admin = KeycloakAdmin(connection=keycloak_connection)
    return keycloak_admin
