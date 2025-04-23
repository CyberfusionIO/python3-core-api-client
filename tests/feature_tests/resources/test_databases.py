from cyberfusion.CoreApiClient.connector import CoreApiConnector
from tests.conftest import DatabaseUpdateRequestFactory, DatabaseCreateRequestFactory
import faker


def test_create_database(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    database_create_request_factory: DatabaseCreateRequestFactory,
) -> None:
    api_connector.databases.create_database(database_create_request_factory.build())


def test_update_database(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    database_update_request_factory: DatabaseUpdateRequestFactory,
) -> None:
    api_connector.databases.update_database(
        database_update_request_factory.build(), id_=faker.pyint()
    )


def test_read_database(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.databases.read_database(id_=faker.pyint())


def test_delete_database(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.databases.delete_database(id_=faker.pyint())


def test_compare_databases(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.databases.compare_databases(
        left_database_id=faker.pyint(), right_database_id=faker.pyint()
    )


def test_sync_databases(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.databases.sync_databases(
        left_database_id=faker.pyint(), right_database_id=faker.pyint()
    )


def test_list_databases(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.databases.list_databases()


def test_list_database_usages(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.databases.list_database_usages(
        database_id=faker.pyint(), timestamp=faker.date_time()
    )
