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


def create_admin_connection(connection_config_object):
    """
    Creates and returns keycloak admin connection with given args

    Args:
        connection_config_object(dict): A dictionary which is expected to contain the following items:
            server_url(str): The url of our keycloak server..
            username(str): The username of the user that has admin priveleges on the server.
            password(str): The password of the user that has admin priveleges on the server.
            realm_name(str): The name of the keycloak realm that we are attempting to access.
            client_id(str): The keycloak client_id that we are using for the connection.
            client_secret_key(str): The secret key of the keycloak client.

    Raises:
        InvalidConnectionException: If the connection arguments are missing and the connection will
            be unable to complete

    Returns:
        keycloak_admin: This object is what holds our connection to the keycloak admin, through this
            we are able to manipulate users and other data depending on the keycloak permissions.
    """
    if list(connection_config_object.keys()) != ADMIN_ARG_LIST:
        missing_args = [
            arg for arg in ADMIN_ARG_LIST if arg not in list(connection_config_object.keys())]
        raise InvalidConnectionException(missing_args=missing_args)

    keycloak_connection = KeycloakOpenIDConnection(
        server_url=connection_config_object.get("server_url"),
        username=connection_config_object.get("username"),
        password=connection_config_object.get("password"),
        realm_name=connection_config_object.get("realm_name"),
        client_id=connection_config_object.get("client_id"),
        client_secret_key=connection_config_object.get("client_secret_key"),
        verify=True,
    )
    keycloak_admin = KeycloakAdmin(connection=keycloak_connection)
    return keycloak_admin
