import json

import faker

from cyberfusion.CoreApiClient.http import Response


def test_Response_attributes(faker: faker.Faker) -> None:
    status_code = faker.http_status_code()
    body = faker.word()
    headers = {}

    response = Response(status_code=status_code, body=body, headers=headers)

    assert response.status_code == status_code
    assert response.body == body
    assert response.headers == headers


def test_Response_failed(faker: faker.Faker) -> None:
    response = Response(status_code=400, body=faker.word(), headers={})

    assert response.failed is True


def test_Response_not_failed(faker: faker.Faker) -> None:
    response = Response(status_code=200, body=faker.word(), headers={})

    assert response.failed is False


def test_Response_body(faker: faker.Faker) -> None:
    body = json.dumps(faker.word())

    response = Response(status_code=faker.http_status_code(), body=body, headers={})

    assert response.body == body


def test_Response_json(faker: faker.Faker) -> None:
    body = json.dumps(faker.word())

    response = Response(status_code=faker.http_status_code(), body=body, headers={})

    assert response.json == json.loads(body)
