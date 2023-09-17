"""
This Module contains a function which provides a keycloak connection
set up as a non privileged user for our main class.
"""
from keycloak import KeycloakOpenID
from orodha_keycloak.connections.exceptions import InvalidConnectionException

CLIENT_ARG_LIST = ["server_url", "realm_name",
                   "client_id", "client_secret_key"]


def create_client_connection(connection_config_object):
    """
    Creates and returns keycloak admin connection with given args

    Args:
        connection_config_object(dict): A dictionary which is expected to contain the following items:
            server_url(str): Url of the keycloak server.
            realm_name(str): The name of the keycloak realm that we are attempting to access.
            client_id(str): The keycloak client_id that we are using for the connection.
            client_secret_key(str): The secret key of the keycloak client.

    Raises:
        InvalidConnectionException: If the connection arguments are missing and the connection will
            be unable to complete

    Returns:
        client_connection: This object is what holds our connection to the keycloak client, through this
            we are able to interact with decoding mechanisms for our jwt tokens.
    """
    if CLIENT_ARG_LIST not in connection_config_object.keys():
        missing_args = [
             arg for arg in CLIENT_ARG_LIST if arg not in list(connection_config_object.keys())]
        raise InvalidConnectionException(missing_args=missing_args)

    client_connection = KeycloakOpenID(
        server_url=connection_config_object.get("server_url"),
        client_id=connection_config_object.get("client_id"),
        realm_name=connection_config_object.get("realm_name"),
        client_secret_key=connection_config_object.get("client_secret_key"),
        verify=True,
    )
    return client_connection
