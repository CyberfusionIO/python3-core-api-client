from cyberfusion.CoreApiClient.connector import CoreApiConnector
from tests.conftest import (
    DatabaseUserUpdateRequestFactory,
    DatabaseUserCreateRequestFactory,
)
import faker


def test_create_database_user(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    database_user_create_request_factory: DatabaseUserCreateRequestFactory,
) -> None:
    api_connector.database_users.create_database_user(
        database_user_create_request_factory.build()
    )


def test_update_database_user(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    database_user_update_request_factory: DatabaseUserUpdateRequestFactory,
) -> None:
    api_connector.database_users.update_database_user(
        database_user_update_request_factory.build(), id_=faker.pyint()
    )


def test_read_database_user(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.database_users.read_database_user(id_=faker.pyint())


def test_delete_database_user(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.database_users.delete_database_user(id_=faker.pyint())


def test_list_database_users(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.database_users.list_database_users()
