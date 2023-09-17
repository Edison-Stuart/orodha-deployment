"""
This Module contains the KeycloakConnection class which is a facade
used to interact with a keycloak server via python-keycloak.
"""
import orodha_keycloak.connections.admin
import orodha_keycloak.connections.client


class KeycloakConnection:
    """
        Facade class used for connecting to, and interacting with keycloak for the Orodha
    shopping list app.

    Args:
        connection_kwargs(dict):
            server_url(str): The url of the server that our keycloak is hosted at
            username(str): The username of the Admin server_user.
            password(str): The password of the Admin server_user.
            realm_name(str): The name of the keycloak realm that we are attempting to access.
            client_id(str): The keycloak client_id that we are using for the connection.
            client_secret_key(str): The secret key of the keycloak client.

    Raises:
        InvalidConnectionException: If the connection variables given are invalid
            and do not allow connection.
    """

    def __init__(self, **connection_kwargs):
        args = {key: value for key, value in connection_kwargs.items()}

        self.admin_connection = orodha_keycloak.connections.admin.create_admin_connection(
            args)
        self.client_connection = orodha_keycloak.connections.client.create_client_connection(
            args)

    def add_user(self, **user_info):
        """
        Adds a user to keycloak with a password.

        Args:
            user_info(kwargs):
                email(str): The email of the new user.
                username(str): The username of the new user.
                firstName(str): The first name of the new user.
                lastName(str): The last name of the new user.
                password(str): The password of the new user.

        Returns:
            new_user: The new user info genereated by the keycloak server.

        """
        new_user = self.admin_connection.create_user(
            {
                "email": user_info.get("email"),
                "username": user_info.get("username"),
                "enabled": True,
                "firstName": user_info.get("firstName"),
                "lastName": user_info.get("lastName"),
                "credentials": [
                    {
                        "value": user_info.get("password"),
                        "type": "password",
                    }
                ],
            },
            exist_ok=False,
        )

        return new_user

    def delete_user(self, user_id):
        """
        Deletes a keycloak user with a given user_id.

        Args:
            user_id(str): The user id of the user to be deleted.

        Returns:
            response: The response from the keycloak server with info about the deletion.
        """
        response = self.admin_connection.delete_user(user_id=user_id)

        return response

    def get_user_from_access_token(self, user_identification, is_token=False):
        """
        Takes either a user_id or username and checks if a certain user exists.

        Args:
            user_identification(str|dict): Can either be a user_id or a JWT token,
                is used to access keycloak in a query.
            is_token(bool): A boolean value that determines if we use user_id or
                token in our keycloak call. If True, we use the user_identification
                variable as if it were a JWT token.

        Returns:
            user: The user, if any, that is associated with this user_identification value.
        """

        # NOTE: This function will be changed to return only relevant information from the decoded
        #   token once I determine the "shape" of the response data.
        if is_token:
            return_value = self._decode_jwt(user_identification)
        else:
            return_value = self.admin_connection.get_user(user_identification)

        return return_value

    def _decode_jwt(self, token):
        """
        Small helper function which decodes a JWT token using the client connection.

        Args:
            token(dict): A JWT token that we get from keycloak.

        Returns:
            token_info(dict): The decoded information from the token.
        """
        keycloak_public_key = "-----BEGIN PUBLIC KEY-----\n" + \
            self.client_connection.public_key() + "\n-----END PUBLIC KEY-----"
        options = {
            "verify_signature": True,
            "verify_aud": True,
            "verify_exp": True
        }
        token_info = self.client_connection.decode_token(
            token,
            key=keycloak_public_key, options=options)
        return token_info
