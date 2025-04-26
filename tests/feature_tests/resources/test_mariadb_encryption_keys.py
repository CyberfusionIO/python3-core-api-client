from cyberfusion.CoreApiClient.connector import CoreApiConnector
from tests.conftest import MariadbEncryptionKeyCreateRequestFactory
import faker


def test_create_mariadb_encryption_key(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    mariadb_encryption_key_create_request_factory: MariadbEncryptionKeyCreateRequestFactory,
) -> None:
    api_connector.mariadb_encryption_keys.create_mariadb_encryption_key(
        mariadb_encryption_key_create_request_factory.build()
    )


def test_read_mariadb_encryption_key(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.mariadb_encryption_keys.read_mariadb_encryption_key(id_=faker.pyint())


def test_list_mariadb_encryption_keys(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.mariadb_encryption_keys.list_mariadb_encryption_keys()
