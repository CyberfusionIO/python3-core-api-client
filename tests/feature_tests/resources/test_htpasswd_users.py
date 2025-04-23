from cyberfusion.CoreApiClient.connector import CoreApiConnector
from tests.conftest import (
    HtpasswdUserUpdateRequestFactory,
    HtpasswdUserCreateRequestFactory,
)
import faker


def test_create_htpasswd_user(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    htpasswd_user_create_request_factory: HtpasswdUserCreateRequestFactory,
) -> None:
    api_connector.htpasswd_users.create_htpasswd_user(
        htpasswd_user_create_request_factory.build()
    )


def test_update_htpasswd_user(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    htpasswd_user_update_request_factory: HtpasswdUserUpdateRequestFactory,
) -> None:
    api_connector.htpasswd_users.update_htpasswd_user(
        htpasswd_user_update_request_factory.build(), id_=faker.pyint()
    )


def test_read_htpasswd_user(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.htpasswd_users.read_htpasswd_user(id_=faker.pyint())


def test_delete_htpasswd_user(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.htpasswd_users.delete_htpasswd_user(id_=faker.pyint())


def test_list_htpasswd_users(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.htpasswd_users.list_htpasswd_users()
