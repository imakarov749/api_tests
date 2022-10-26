from requests import Response
from pytest_voluptuous import S
from utils.base_session import reqres_session
import schemas.reqres_schemas as schema


def test_create_user():
    name = "Ivan Ivanov"
    job = "qa"

    result: Response = reqres_session().post(
        url="/api/users",
        json={"name": name, "job": job}
    )

    assert result.status_code == 201
    assert result.json()['name'] == name
    assert result.json()['job'] == job
    assert isinstance(result.json()['id'], str)
    assert result.json() == S(schema.create_user_schema)
