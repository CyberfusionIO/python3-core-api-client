import json
from http import HTTPStatus

import pytest
from cyberfusion.CoreApiClient.connector import CoreApiConnector
import faker
from requests_mock import Mocker


def test_duplicate_jwt_and_api_key(
    faker: faker.Faker,
    base_url: str,
) -> None:
    username = faker.user_name()
    password = faker.password()
    api_key = faker.user_name()

    with pytest.raises(
        ValueError, match="^Specify either username and password, or API key, not both$"
    ):
        CoreApiConnector(
            base_url=base_url, username=username, password=password, api_key=api_key
        )


def test_missing_jwt_and_api_key(
    faker: faker.Faker,
    base_url: str,
) -> None:
    with pytest.raises(
        ValueError, match="^Specify either username and password, or API key$"
    ):
        CoreApiConnector(base_url=base_url, username=None, password=None, api_key=None)


def test_username_without_password(
    faker: faker.Faker,
    base_url: str,
) -> None:
    username = faker.user_name()

    with pytest.raises(
        ValueError, match="^If username is specified, password must be specified$"
    ):
        CoreApiConnector(base_url=base_url, username=username, password=None)


def test_password_without_username(
    faker: faker.Faker,
    base_url: str,
) -> None:
    password = faker.password()

    with pytest.raises(
        ValueError, match="^If password is specified, username must be specified$"
    ):
        CoreApiConnector(base_url=base_url, username=None, password=password)


def test_attributes_jwt(faker: faker.Faker, base_url: str) -> None:
    username = faker.user_name()
    password = faker.password()

    api_connector = CoreApiConnector(
        base_url=base_url,
        username=username,
        password=password,
    )

    assert api_connector.base_url == base_url
    assert api_connector.username == username
    assert api_connector.password == password
    assert api_connector.api_key is None
    assert api_connector.requests_session is not None
    assert api_connector._jwt_metadata is None


def test_attributes_api_key(faker: faker.Faker, base_url: str) -> None:
    api_key = faker.user_name()

    api_connector = CoreApiConnector(base_url=base_url, api_key=api_key)

    assert api_connector.base_url == base_url
    assert api_connector.api_key == api_key
    assert api_connector.username is None
    assert api_connector.password is None
    assert api_connector.requests_session is not None
    assert api_connector._jwt_metadata is None


def test_authentication_headers_jwt(
    faker: faker.Faker, base_url: str, requests_mock: Mocker
) -> None:
    access_token = faker.word()

    requests_mock.post(
        "".join([base_url, "/api/v1/login/access-token"]),
        json={
            "access_token": access_token,
            "token_type": "bearer",
            "expires_in": faker.pyint(),
        },
        status_code=HTTPStatus.OK,
    )

    username = faker.user_name()
    password = faker.password()

    api_connector = CoreApiConnector(
        base_url=base_url,
        username=username,
        password=password,
    )

    assert api_connector.authentication_headers == {
        "Authorization": "Bearer " + access_token,
    }


def test_authentication_headers_api_key(
    faker: faker.Faker, base_url: str, requests_mock: Mocker
) -> None:
    api_key = faker.user_name()

    api_connector = CoreApiConnector(base_url=base_url, api_key=api_key)

    assert api_connector.authentication_headers == {
        "X-API-Key": api_key,
    }


def test_send_content_type_default(
    faker: faker.Faker, base_url: str, requests_mock: Mocker
) -> None:
    username = faker.user_name()
    password = faker.password()

    requests_mock.post(
        "".join([base_url, "/api/v1/login/access-token"]), real_http=True
    )

    noop_mock = requests_mock.get(
        "".join([base_url, "/api/v1/noop"]), json={}, status_code=HTTPStatus.OK
    )

    api_connector = CoreApiConnector(
        base_url=base_url,
        username=username,
        password=password,
    )

    api_connector.send("GET", "/api/v1/noop")

    assert noop_mock.last_request.headers["Content-Type"] == "application/json"


def test_send_content_type_custom(
    faker: faker.Faker, base_url: str, requests_mock: Mocker
) -> None:
    username = faker.user_name()
    password = faker.password()
    content_type = faker.word()

    requests_mock.post(
        "".join([base_url, "/api/v1/login/access-token"]), real_http=True
    )

    noop_mock = requests_mock.get(
        "".join([base_url, "/api/v1/noop"]), json={}, status_code=HTTPStatus.OK
    )

    api_connector = CoreApiConnector(
        base_url=base_url,
        username=username,
        password=password,
    )

    api_connector.send("GET", "/api/v1/noop", content_type=content_type)

    assert noop_mock.last_request.headers["Content-Type"] == content_type


def test_send_json_dumped_when_content_type_json(
    faker: faker.Faker, base_url: str, requests_mock: Mocker
) -> None:
    username = faker.user_name()
    password = faker.password()

    DICT = {"key": "value"}

    requests_mock.post(
        "".join([base_url, "/api/v1/login/access-token"]), real_http=True
    )

    noop_mock = requests_mock.post(
        "".join([base_url, "/api/v1/noop"]), json={}, status_code=HTTPStatus.OK
    )

    api_connector = CoreApiConnector(
        base_url=base_url,
        username=username,
        password=password,
    )

    api_connector.send(
        "POST", "/api/v1/noop", data=DICT, content_type="application/json"
    )

    assert noop_mock.last_request.body == json.dumps(DICT)


def test_send_json_not_dumped_when_not_content_type_json(
    faker: faker.Faker, base_url: str, requests_mock: Mocker
) -> None:
    username = faker.user_name()
    password = faker.password()
    content_type = faker.word()

    DICT = {"key": "value"}

    requests_mock.post(
        "".join([base_url, "/api/v1/login/access-token"]), real_http=True
    )

    noop_mock = requests_mock.post(
        "".join([base_url, "/api/v1/noop"]), json={}, status_code=HTTPStatus.OK
    )

    api_connector = CoreApiConnector(
        base_url=base_url,
        username=username,
        password=password,
    )

    api_connector.send("POST", "/api/v1/noop", data=DICT, content_type=content_type)

    assert noop_mock.last_request.body == "key=value"


def test_send_json_datetime_serialised(
    faker: faker.Faker, base_url: str, requests_mock: Mocker
) -> None:
    username = faker.user_name()
    password = faker.password()

    VALUE = faker.date_time()

    requests_mock.post(
        "".join([base_url, "/api/v1/login/access-token"]), real_http=True
    )

    noop_mock = requests_mock.post(
        "".join([base_url, "/api/v1/noop"]), json={}, status_code=HTTPStatus.OK
    )

    api_connector = CoreApiConnector(
        base_url=base_url,
        username=username,
        password=password,
    )

    api_connector.send(
        "POST", "/api/v1/noop", data=VALUE, content_type="application/json"
    )

    assert str(VALUE.year) in noop_mock.last_request.body


def test_send_query_parameters_datetime_serialised(
    faker: faker.Faker, base_url: str, requests_mock: Mocker
) -> None:
    username = faker.user_name()
    password = faker.password()

    KEY = faker.word()
    VALUE = faker.date_time()

    requests_mock.post(
        "".join([base_url, "/api/v1/login/access-token"]), real_http=True
    )

    noop_mock = requests_mock.post(
        "".join([base_url, "/api/v1/noop"]), json={}, status_code=HTTPStatus.OK
    )

    api_connector = CoreApiConnector(
        base_url=base_url,
        username=username,
        password=password,
    )

    api_connector.send(
        "POST",
        "/api/v1/noop",
        query_parameters={KEY: VALUE},
    )

    assert str(VALUE.year) in noop_mock.last_request.qs[KEY][0]


def test_send_or_fail_with_auto_pagination_single_page(
    faker: faker.Faker, base_url: str, requests_mock: Mocker
) -> None:
    api_key = faker.user_name()

    items = [{"id": 1}, {"id": 2}]

    requests_mock.get(
        "".join([base_url, "/api/v1/items"]),
        json=items,
        status_code=HTTPStatus.OK,
    )

    api_connector = CoreApiConnector(base_url=base_url, api_key=api_key)

    responses = api_connector.send_or_fail_with_auto_pagination("GET", "/api/v1/items")

    assert len(responses) == 1
    assert responses[0].json == items
    assert responses[0].status_code == HTTPStatus.OK


def test_send_or_fail_with_auto_pagination_multiple_pages(
    faker: faker.Faker, base_url: str, requests_mock: Mocker
) -> None:
    api_key = faker.user_name()

    page1_items = [{"id": 1}, {"id": 2}]
    page2_items = [{"id": 3}, {"id": 4}]
    page3_items = [{"id": 5}]

    responses = [
        {
            "json": page1_items,
            "status_code": HTTPStatus.OK,
            "headers": {
                "link": '<https://example.com/api/v1/items?page=2>; rel="next"'
            },
        },
        {
            "json": page2_items,
            "status_code": HTTPStatus.OK,
            "headers": {
                "link": '<https://example.com/api/v1/items?page=3>; rel="next"'
            },
        },
        {
            "json": page3_items,
            "status_code": HTTPStatus.OK,
            "headers": {},
        },
    ]

    requests_mock.get(
        "".join([base_url, "/api/v1/items"]),
        responses,
    )

    api_connector = CoreApiConnector(base_url=base_url, api_key=api_key)

    pagination_responses = api_connector.send_or_fail_with_auto_pagination(
        "GET", "/api/v1/items"
    )

    assert len(pagination_responses) == 3
    assert pagination_responses[0].json == page1_items
    assert pagination_responses[1].json == page2_items
    assert pagination_responses[2].json == page3_items


def test_send_or_fail_with_auto_pagination_default_per_page(
    faker: faker.Faker, base_url: str, requests_mock: Mocker
) -> None:
    api_key = faker.user_name()

    mock = requests_mock.get(
        "".join([base_url, "/api/v1/items"]),
        json=[],
        status_code=HTTPStatus.OK,
    )

    api_connector = CoreApiConnector(base_url=base_url, api_key=api_key)

    api_connector.send_or_fail_with_auto_pagination("GET", "/api/v1/items")

    assert mock.last_request.qs["per_page"] == ["50"]
    assert mock.last_request.qs["page"] == ["1"]
