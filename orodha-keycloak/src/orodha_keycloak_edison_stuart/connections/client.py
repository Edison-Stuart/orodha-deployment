from keycloak import KeycloakOpenID
from . import CLIENT_ARG_LIST
from exceptions import InvalidConnectionException


def create_client_connection(**kwargs):
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
    if list(kwargs.keys()) != CLIENT_ARG_LIST:
        missing_args = [
            arg for arg in CLIENT_ARG_LIST if arg not in list(kwargs.keys())]
        raise InvalidConnectionException(missing_args=missing_args)

    client_connection = KeycloakOpenID(
        server_url=kwargs.get("server_user"),
        client_id=kwargs.get("client_id"),
        client_secret_key=kwargs.get("client_secret_key"),
        verify=True
    )
    return client_connection


"""
Test this out in a container w/access to your running keycloak...

token = keycloak_openid.token("user", "password")

KEYCLOAK_PUBLIC_KEY = "-----BEGIN PUBLIC KEY-----\n" + keycloak_openid.public_key() + "\n-----END PUBLIC KEY-----"
options = {"verify_signature": True, "verify_aud": True, "verify_exp": True}
token_info = keycloak_openid.decode_token(token['access_token'], key=KEYCLOAK_PUBLIC_KEY, options=options)
print(token_info)
"""
# so that we can...


def decode_jwt(token):
    KEYCLOAK_PUBLIC_KEY = "-----BEGIN PUBLIC KEY-----\n" + \
        keycloak_openid.public_key() + "\n-----END PUBLIC KEY-----"
    options = {"verify_signature": True,
               "verify_aud": True, "verify_exp": True}
    token_info = keycloak_openid.decode_token(
        token['access_token'], key=KEYCLOAK_PUBLIC_KEY, options=options)
    return token_info
