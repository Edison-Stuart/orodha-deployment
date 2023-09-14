MOCK_DATA = {
    "create_user_request":
        {
            "email": "email@example.com",
            "username": "myuser",
            "firstName": "John",
            "lastName": "Doe",
            "credentials": [
                {
                        "value": "password",
                        "type": "password",
                }
            ],
        },
    "create_user_response": {
        "user_data": {
            "some_data": None
        },
        "code": 200
            },
    "delete_user_response": {
        "message": "user_deleted",
        "code": 200
            }
}
