import json

import requests
from cyberfusion.CoreApiClient.connector import CoreApiConnector
import faker
import pytest
from requests_mock import Mocker
import urllib.parse
import time
from urllib.parse import urljoin, urlparse
from cyberfusion.CoreApiClient.exceptions import AuthenticationException, CallException
from cyberfusion.CoreApiClient.http import Response


def test_initial_login(
    faker: faker.Faker, base_url: str, requests_mock: Mocker
) -> None:
    access_token = faker.word()

    login_mock = requests_mock.post(
        "".join([base_url, "/api/v1/login/access-token"]),
        json={
            "access_token": access_token,
            "token_type": "bearer",
            "expires_in": faker.pyint(),
        },
        status_code=200,
    )

    requests_mock.get("".join([base_url, "/api/v1/noop"]), real_http=True)

    username = faker.user_name()
    password = faker.password()

    api_connector = CoreApiConnector(
        base_url=base_url,
        username=username,
        password=password,
    )

    api_connector.send("GET", "/api/v1/noop")

    assert login_mock.called_once

    assert login_mock.last_request.method == "POST"
    assert login_mock.last_request.url == "".join(
        [base_url, "/api/v1/login/access-token"]
    )
    assert (
        login_mock.last_request.headers["Content-Type"]
        == "application/x-www-form-urlencoded"
    )
    assert (
        login_mock.last_request.text
        == f"username={username}&password={urllib.parse.quote_plus(password)}"
    )


def test_single_login(faker: faker.Faker, base_url: str, requests_mock: Mocker) -> None:
    access_token = faker.word()

    login_mock = requests_mock.post(
        "".join([base_url, "/api/v1/login/access-token"]),
        json={
            "access_token": access_token,
            "token_type": "bearer",
            "expires_in": faker.pyint(),
        },
        status_code=200,
    )

    noop_mock = requests_mock.get(
        "".join([base_url, "/api/v1/noop"]), json={}, status_code=200
    )

    username = faker.user_name()
    password = faker.password()

    api_connector = CoreApiConnector(
        base_url=base_url,
        username=username,
        password=password,
    )

    api_connector.send("GET", "/api/v1/noop")
    api_connector.send("GET", "/api/v1/noop")

    assert noop_mock.call_count == 2

    assert login_mock.called_once


def test_jwt_token_renewed(
    faker: faker.Faker, base_url: str, requests_mock: Mocker
) -> None:
    access_token = faker.word()
    expires_in = 1

    login_mock = requests_mock.post(
        "".join([base_url, "/api/v1/login/access-token"]),
        json={
            "access_token": access_token,
            "token_type": "bearer",
            "expires_in": expires_in,
        },
        status_code=200,
    )

    requests_mock.get("".join([base_url, "/api/v1/noop"]), real_http=True)

    username = faker.user_name()
    password = faker.password()

    api_connector = CoreApiConnector(
        base_url=base_url,
        username=username,
        password=password,
    )

    api_connector.send("GET", "/api/v1/noop")

    assert login_mock.call_count == 1

    time.sleep(expires_in + 1)

    api_connector.send("GET", "/api/v1/noop")

    assert login_mock.call_count == 2


def test_authentication_exception(
    faker: faker.Faker, base_url: str, requests_mock: Mocker
) -> None:
    login_mock = requests_mock.post(
        "".join([base_url, "/api/v1/login/access-token"]),
        json={"detail": faker.word()},
        status_code=403,
    )

    username = faker.user_name()
    password = faker.password()

    api_connector = CoreApiConnector(
        base_url=base_url,
        username=username,
        password=password,
    )

    with pytest.raises(AuthenticationException):
        api_connector.send("GET", "/api/v1/noop")

    assert login_mock.called_once


def test_send_success(faker: faker.Faker, base_url: str, requests_mock: Mocker) -> None:
    JSON = {}
    STATUS_CODE = 200

    requests_mock.post(
        "".join([base_url, "/api/v1/login/access-token"]), real_http=True
    )

    requests_mock.get(
        "".join([base_url, "/api/v1/noop"]), json=JSON, status_code=STATUS_CODE
    )

    username = faker.user_name()
    password = faker.password()

    api_connector = CoreApiConnector(
        base_url=base_url,
        username=username,
        password=password,
    )

    response = api_connector.send("GET", "/api/v1/noop")

    assert isinstance(response, Response)

    assert response.status_code == 200
    assert response.body == json.dumps(JSON)
    assert response.headers == {}
    assert response.json == JSON
    assert response.failed is False


def test_send_failed(faker: faker.Faker, base_url: str, requests_mock: Mocker) -> None:
    JSON = {"detail": faker.word()}
    STATUS_CODE = 400

    requests_mock.post(
        "".join([base_url, "/api/v1/login/access-token"]), real_http=True
    )

    requests_mock.get(
        "".join([base_url, "/api/v1/noop"]), json=JSON, status_code=STATUS_CODE
    )

    username = faker.user_name()
    password = faker.password()

    api_connector = CoreApiConnector(
        base_url=base_url,
        username=username,
        password=password,
    )

    response = api_connector.send("GET", "/api/v1/noop")

    assert isinstance(response, Response)

    assert response.status_code == STATUS_CODE
    assert response.body == json.dumps(JSON)
    assert response.headers == {}
    assert response.json == JSON
    assert response.failed is True


def test_send_or_fail_success(
    faker: faker.Faker, base_url: str, requests_mock: Mocker
) -> None:
    JSON = {}
    STATUS_CODE = 200

    requests_mock.post(
        "".join([base_url, "/api/v1/login/access-token"]), real_http=True
    )

    requests_mock.get(
        "".join([base_url, "/api/v1/noop"]), json=JSON, status_code=STATUS_CODE
    )

    username = faker.user_name()
    password = faker.password()

    api_connector = CoreApiConnector(
        base_url=base_url,
        username=username,
        password=password,
    )

    response = api_connector.send_or_fail("GET", "/api/v1/noop")

    assert isinstance(response, Response)

    assert response.status_code == 200
    assert response.body == json.dumps(JSON)
    assert response.headers == {}
    assert response.json == JSON
    assert response.failed is False


def test_send_or_fail_failed(
    faker: faker.Faker, base_url: str, requests_mock: Mocker
) -> None:
    JSON = {"detail": faker.word()}
    STATUS_CODE = 400

    requests_mock.post(
        "".join([base_url, "/api/v1/login/access-token"]), real_http=True
    )

    requests_mock.get(
        "".join([base_url, "/api/v1/noop"]), json=JSON, status_code=STATUS_CODE
    )

    username = faker.user_name()
    password = faker.password()

    api_connector = CoreApiConnector(
        base_url=base_url,
        username=username,
        password=password,
    )

    with pytest.raises(CallException) as e:
        api_connector.send_or_fail("GET", "/api/v1/noop")

    assert isinstance(e.value, CallException)

    assert e.value.body == json.dumps(JSON)
    assert e.value.status_code == STATUS_CODE


def test_custom_requests_session(
    faker: faker.Faker, base_url: str, requests_mock: Mocker
) -> None:
    username = faker.user_name()
    password = faker.password()
    user_agent = faker.word()

    requests_mock.post(
        "".join([base_url, "/api/v1/login/access-token"]), real_http=True
    )

    noop_mock = requests_mock.get(
        "".join([base_url, "/api/v1/noop"]), json={}, status_code=200
    )

    requests_session = requests.Session()
    requests_session.headers.update({"User-Agent": user_agent})

    api_connector = CoreApiConnector(
        base_url=base_url,
        username=username,
        password=password,
        requests_session=requests_session,
    )

    assert api_connector.requests_session == requests_session

    api_connector.send("GET", "/api/v1/noop")

    assert noop_mock.called_once

    assert noop_mock.last_request.headers["User-Agent"] == user_agent


def test_default_requests_session(
    faker: faker.Faker,
    base_url: str,
) -> None:
    username = faker.user_name()
    password = faker.password()

    api_connector = CoreApiConnector(
        base_url=base_url,
        username=username,
        password=password,
        requests_session=None,
    )

    assert isinstance(api_connector.requests_session, requests.Session)


def test_send_request(faker: faker.Faker, base_url: str, requests_mock: Mocker) -> None:
    JSON = {}
    STATUS_CODE = 200

    DATA = faker.pydict(value_types=str)
    QUERY_PARAMETERS = faker.pydict(value_types=str)
    METHOD = "POST"

    requests_mock.post(
        "".join([base_url, "/api/v1/login/access-token"]), real_http=True
    )

    noop_mock = requests_mock.post(
        "".join([base_url, "/api/v1/noop"]),
        json=JSON,
        status_code=STATUS_CODE,
    )

    username = faker.user_name()
    password = faker.password()

    api_connector = CoreApiConnector(
        base_url=base_url,
        username=username,
        password=password,
    )

    api_connector.send(
        METHOD, "/api/v1/noop", data=DATA, query_parameters=QUERY_PARAMETERS
    )

    assert noop_mock.called_once

    assert noop_mock.last_request.method == METHOD
    assert urljoin(
        noop_mock.last_request.url, urlparse(noop_mock.last_request.url).path
    ) == "".join([base_url, "/api/v1/noop"])
    assert noop_mock.last_request.json() == DATA
    assert noop_mock.last_request.qs == {
        key: [value.lower()] for key, value in QUERY_PARAMETERS.items()
    }
