"""
This module contains our KeycloakConnection mock class which provides an interface for
interacting with the python-keycloak package without having a live connection.
"""
import unittest.mock


class MockKeycloakConnection(unittest.mock.MagicMock):
    """
    A mock class for testing that our functions are called with correct values.
    """
    def __init__(self, mock_create_admin_connection):
        self.connection = mock_create_admin_connection()
        super().__init__(self)

    def add_user(self, **user_info):
        try:
            new_user = self.connection.create_user(
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
                exist_ok=False
            )
        except Exception as exception:
            raise Exception from exception

        return new_user

    def delete_keycloak_user(self, user_id):
        try:
            response = self.connection.delete_user(user_id=user_id)
        except Exception as exception:
            raise Exception from exception

        return response
