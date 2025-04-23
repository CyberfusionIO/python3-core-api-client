from cyberfusion.CoreApiClient.connector import CoreApiConnector
from tests.conftest import UnixUserUpdateRequestFactory, UnixUserCreateRequestFactory
import faker


def test_create_unix_user(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    unix_user_create_request_factory: UnixUserCreateRequestFactory,
) -> None:
    api_connector.unix_users.create_unix_user(unix_user_create_request_factory.build())


def test_update_unix_user(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    unix_user_update_request_factory: UnixUserUpdateRequestFactory,
) -> None:
    api_connector.unix_users.update_unix_user(
        unix_user_update_request_factory.build(), id_=faker.pyint()
    )


def test_read_unix_user(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.unix_users.read_unix_user(id_=faker.pyint())


def test_delete_unix_user(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.unix_users.delete_unix_user(id_=faker.pyint())


def test_compare_unix_users(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.unix_users.compare_unix_users(
        left_unix_user_id=faker.pyint(), right_unix_user_id=faker.pyint()
    )


def test_list_unix_users(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.unix_users.list_unix_users()


def test_list_unix_user_usages(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.unix_users.list_unix_user_usages(
        unix_user_id=faker.pyint(), timestamp=faker.date_time()
    )
