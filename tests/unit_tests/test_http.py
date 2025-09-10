import json
from http import HTTPStatus

import faker

from cyberfusion.CoreApiClient.http import Response
from requests import Response as RequestsResponse


def test_Response_attributes(faker: faker.Faker) -> None:
    status_code = faker.http_status_code()
    body = faker.word()
    headers = {}

    response = Response(
        status_code=status_code,
        body=body,
        headers=headers,
        requests_response=RequestsResponse(),
    )

    assert response.status_code == status_code
    assert response.body == body
    assert response.headers == headers


def test_Response_failed(faker: faker.Faker) -> None:
    response = Response(
        status_code=HTTPStatus.BAD_REQUEST,
        body=faker.word(),
        headers={},
        requests_response=RequestsResponse(),
    )

    assert response.failed is True


def test_Response_not_failed(faker: faker.Faker) -> None:
    response = Response(
        status_code=HTTPStatus.OK,
        body=faker.word(),
        headers={},
        requests_response=RequestsResponse(),
    )

    assert response.failed is False


def test_Response_body(faker: faker.Faker) -> None:
    body = json.dumps(faker.word())

    response = Response(
        status_code=faker.http_status_code(),
        body=body,
        headers={},
        requests_response=RequestsResponse(),
    )

    assert response.body == body


def test_Response_json(faker: faker.Faker) -> None:
    body = json.dumps(faker.word())

    response = Response(
        status_code=faker.http_status_code(),
        body=body,
        headers={},
        requests_response=RequestsResponse(),
    )

    assert response.json == json.loads(body)
