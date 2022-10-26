from voluptuous import Schema, PREVENT_EXTRA

create_user_schema = Schema(
    {
        "name": str,
        "job": str,
        "id": str,
        "createdAt": str,
    },
    required=True,
    extra=PREVENT_EXTRA,
)

update_user_schema = Schema(
    {
        "name": str,
        "job": str,
        "updatedAt": str,
    },
    required=True,
    extra=PREVENT_EXTRA,
)

register_user_schema = Schema(
    {
        "id": int,
        "token": str
    },
    required=True,
    extra=PREVENT_EXTRA,
)

login_user_schema = Schema(
    {
        "token": str
    }
)