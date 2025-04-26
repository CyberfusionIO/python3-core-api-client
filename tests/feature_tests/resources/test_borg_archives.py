from cyberfusion.CoreApiClient.connector import CoreApiConnector
from tests.conftest import (
    BorgArchiveCreateUnixUserRequestFactory,
    BorgArchiveCreateDatabaseRequestFactory,
)
import faker


def test_create_borg_archive_for_database(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    borg_archive_create_database_request_factory: BorgArchiveCreateDatabaseRequestFactory,
) -> None:
    api_connector.borg_archives.create_borg_archive_for_database(
        borg_archive_create_database_request_factory.build()
    )


def test_create_borg_archive_for_unix_user(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    borg_archive_create_unix_user_request_factory: BorgArchiveCreateUnixUserRequestFactory,
) -> None:
    api_connector.borg_archives.create_borg_archive_for_unix_user(
        borg_archive_create_unix_user_request_factory.build()
    )


def test_read_borg_archive(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.borg_archives.read_borg_archive(id_=faker.pyint())


def test_get_borg_archive_metadata(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.borg_archives.get_borg_archive_metadata(id_=faker.pyint())


def test_restore_borg_archive(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.borg_archives.restore_borg_archive(id_=faker.pyint())


def test_download_borg_archive(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.borg_archives.download_borg_archive(id_=faker.pyint())


def test_list_borg_archives(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.borg_archives.list_borg_archives()


def test_list_borg_archive_contents(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.borg_archives.list_borg_archive_contents(id_=faker.pyint())
