"""
This Module contains a function which provides a keycloak connection
set up as an admin for our main class.
"""
from keycloak import KeycloakAdmin, KeycloakOpenIDConnection

class InvalidConnectionException(Exception):
    """
    Exception for when connection arguments are missing or invalid

    Args:
        missing_args(list[str]): A list of the missing argument keys.
        message(str): An optional message to be displayed when raised.
    """
    def __init__(self, missing_args:list, message:str=None):
        if message is None:
            message = "Missing connection args:"
            for arg in missing_args:
                message.append(" "+arg)
            super().__init__(message)
        self.message = message


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
    arg_list = [
			"server_url",
			"username",
			"password",
			"realm_name",
			"client_id",
			"client_secret_key"
			]
    if list(kwargs.keys()) != arg_list:
        missing_args = [arg for arg in arg_list if arg not in list(kwargs.keys())]
        raise InvalidConnectionException(missing_args=missing_args)

    keycloak_connection = KeycloakOpenIDConnection(
        server_url=kwargs["server_user"],
        username=kwargs["username"],
        password=kwargs["password"],
        realm_name=kwargs["realm_name"],
        client_id=kwargs["client_id"],
        client_secret_key=kwargs["client_secret_key"],
        verify=True
    )
    keycloak_admin = KeycloakAdmin(connection=keycloak_connection)
    return keycloak_admin
