import faker

from cyberfusion.CoreApiClient.exceptions import CallException, AuthenticationException


def test_CallException_attributes(faker: faker.Faker) -> None:
    body = faker.word()
    status_code = faker.http_status_code()

    exception = CallException(body=body, status_code=status_code)

    assert exception.body == body
    assert exception.status_code == status_code


def test_AuthenticationException_attributes(faker: faker.Faker) -> None:
    body = faker.word()
    status_code = faker.http_status_code()

    exception = AuthenticationException(body=body, status_code=status_code)

    assert exception.body == body
    assert exception.status_code == status_code
