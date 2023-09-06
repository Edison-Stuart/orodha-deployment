from keycloak import KeycloakAdmin, KeycloakOpenIDConnection

def check_if_user_exists(admin, username):
    return admin.get_user_id(username)


# Admin function 

def delete_keycloak_user():
    pass

def add_keycloak_user():
    pass

if __name__ == "__main__":
    
    keycloak_admin.users_count()
