from requests import Response
from pytest_voluptuous import S
from utils.base_session import reqres_session
import schemas.reqres_schemas as schema


def test_successful_login():
    email = "eve.holt@reqres.in"
    password = "cityslicka"

    result: Response = reqres_session().post(
        url="/api/login",
        json={"email": email, "password": password}
    )
    print(result.text)

    assert result.status_code == 200
    assert result.json() == S(schema.login_user_schema)
