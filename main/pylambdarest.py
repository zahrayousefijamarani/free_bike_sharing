from pylambdarest import route

user_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"}
    },
    "required": ["name"],
    "additionalProperties": False
}

@route(body_schema=user_schema)
def create_user(request):
    # If the request's body does not
    # satisfy the user_schema,
    # a 400 will be returned

    # Create user here

    return 201


query_params_schema = {
    "type": "object",
    "properties": {
        # Only string types are allowed for query parameters.
        # Types casting should be done in the handler.
        "page": {"type": "string"}
    },
    "additionalProperties": False
}

@route(query_params_schema=query_params_schema)
def get_users(request):
    page = int(request.query_params.get("page", 1))

    # request users in db
    users = [
        {"userId": i}
        for i in range((page - 1) * 50, page * 50)
    ]

    return 200, users