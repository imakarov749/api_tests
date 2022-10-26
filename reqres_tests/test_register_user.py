from requests import Response
from pytest_voluptuous import S
from utils.base_session import reqres_session
import schemas.reqres_schemas as schema


def test_user_registration():
    email = "eve.holt@reqres.in"
    password = "cityslicka"

    result: Response = reqres_session().post(
        url="/api/register",
        json={"email": email, "password": password}
    )
    print(result.text)

    assert result.status_code == 200
    assert result.json() == S(schema.register_user_schema)
