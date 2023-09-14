

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
