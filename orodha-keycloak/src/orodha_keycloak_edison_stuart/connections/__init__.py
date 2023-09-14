from .admin import create_admin_connection
from .client import create_client_connection
from .exceptions import InvalidConnectionException
ADMIN_ARG_LIST = [
    "server_url",
    "username",
    "password",
    "realm_name",
    "client_id",
    "client_secret_key"
]

CLIENT_ARG_LIST = [
    "server_url",
    "realm_name",
    "client_id",
    "client_secret_key"
]
