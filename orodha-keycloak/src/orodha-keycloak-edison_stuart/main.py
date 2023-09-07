"""
This Module contains the KeycloakConnection class which is a facade
used to interact with a keycloak server via python-keycloak.
"""
from .connections import create_admin_connection, InvalidConnectionException

class KeycloakConnection():
    """
        Facade class used for connecting to, and interacting with keycloak for the Orodha
    shopping list app.

    Args:
        connection_kwargs:
            server_user: User that has admin priveleges on the server.
		    username: The username of the server_user.
		    password: The password of the server_user.
		    realm_name: The name of the keycloak realm that we are attempting to access.
		    client_id: The keycloak client_id that we are using for the connection.
		    client_secret_key: The secret key of the keycloak client.

    Raises:
        InvalidConnectionException: If the connection variables given are invalid
            and do not allow connection.
    """
    def __init__(self, **connection_kwargs):
        try:
            args = list(connection_kwargs)
            connection = create_admin_connection(*args)
            self.connection = connection
        except InvalidConnectionException as exception:
            raise InvalidConnectionException from exception
        except Exception as exception:
            raise Exception from exception

    def add_user(self, **user_info):
        """
        Adds a user to keycloak with a password.

        Args:
            user_info:
                email: The email of the new user.
                username: The username of the new user.
                firstName: The first name of the new user.
                lastName: The last name of the new user.
                password: The password of the new user.

        Raises:
            Exception: If there is a connection error or keycloak error from the server.

        Returns:
            new_user: The new user info genereated by the keycloak server.

        """
        try:
            new_user = self.connection.create_user(
                {
                    "email": user_info["email"],
                    "username": user_info["username"],
                    "enabled": True,
                    "firstName": user_info["firstName"],
                    "lastName": user_info["lastName"],
                    "credentials": [
                        {
                            "value": user_info["password"],
                            "type": "password",
                        }
                    ],
                },
                exist_ok=False
            )
        except Exception as exception:
            raise Exception from exception

        return new_user

    def delete_keycloak_user(self, user_id):
        """
        Deletes a keycloak user with a given user_id.

        Args:
            user_id: The user id of the user to be deleted.

        Raises:
            Exception: If python-keycloak throws an exception we just re-raise it.

        Returns:
            response: The response from the keycloak server with info about the deletion.
        """
        try:
            response = self.connection.delete_user(user_id=user_id)
        except Exception as exception:
            raise Exception from exception

        return response

    def check_if_user_exists(self, user_identification, user_id=False):
        """
        Takes either a user_id or username and checks if a certain user exists.

        Args:
            user_identification: Can either be a user_id or a username,
                is used to access keycloak in a query.
            user_id(bool): A boolean value that determines if we use user_id or
                username in our keycloak call. If True, we use the user_identification
                variable as if it is a user_id.

        Raises:
            Exception: If There is any issue obtaining a user from the given value.

        Returns:
            user: The user, if any, that is associated with this user_identification value.
        """
        try:
            if user_id:
                user = self.connection.get_user(user_identification)
            else:
                user = self.connection.get_user_id(user_identification)
        except Exception as exception:
            raise Exception from exception

        return user
                