import pytest
from requests import Response
from pytest_voluptuous import S
from utils.base_session import reqres_session
import schemas.reqres_schemas as schema


# постарался сделать так, чтобы переменная из фикстуры передавалась в тесте
# не пойму, получилось или нет, но оно работает
@pytest.mark.parametrize("user_id", [1])
def test_update_user(create_user, user_id):
    name = "Ivan Ivanov"
    job = "builder"

    result: Response = reqres_session().put(
        url=f"/api/users/{create_user}",
        json={"name": name, "job": job}
    )

    print(result.text)
    print(create_user, user_id)

    assert result.status_code == 200
    assert result.json()['name'] == name
    assert result.json()['job'] == job
    assert result.json() == S(schema.update_user_schema)
