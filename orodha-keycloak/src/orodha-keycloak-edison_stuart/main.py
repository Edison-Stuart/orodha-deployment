from http import server
from keycloak import KeycloakAdmin, KeycloakOpenIDConnection

def delete_keycloak_user():
    pass

def check_if_user_exists(admin, username):
    return admin.get_user_id(username)


# Admin function 

def add_keycloak_user():
    pass

if __name__ == "__main__":
    keycloak_connection = KeycloakOpenIDConnection(
        server_url="http://keycloak:8080/auth/",
        username='admin',
        password='password',
        realm_name="user",
        client_id="test_client",
        client_secret_key="o0ZRh7QzFhGrfN95NCLzHHMhuCUslLsF",
        verify=True
    )
    keycloak_admin = KeycloakAdmin(connection=keycloak_connection)
    keycloak_admin.users_count()
