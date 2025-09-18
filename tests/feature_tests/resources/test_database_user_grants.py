from cyberfusion.CoreApiClient.connector import CoreApiConnector
from tests.conftest import DatabaseUserGrantCreateRequestFactory
import faker


def test_create_database_user_grant(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    database_user_grant_create_request_factory: DatabaseUserGrantCreateRequestFactory,
) -> None:
    api_connector.database_user_grants.create_database_user_grant(
        database_user_grant_create_request_factory.build()
    )


def test_list_database_user_grants(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.database_user_grants.list_database_user_grants()


def test_delete_database_user_grant(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.database_user_grants.delete_database_user_grant(id_=faker.pyint())
