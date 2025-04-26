from cyberfusion.CoreApiClient.connector import CoreApiConnector
from tests.conftest import (
    BorgRepositoryUpdateRequestFactory,
    BorgRepositoryCreateRequestFactory,
)
import faker


def test_create_borg_repository(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    borg_repository_create_request_factory: BorgRepositoryCreateRequestFactory,
) -> None:
    api_connector.borg_repositories.create_borg_repository(
        borg_repository_create_request_factory.build()
    )


def test_update_borg_repository(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    borg_repository_update_request_factory: BorgRepositoryUpdateRequestFactory,
) -> None:
    api_connector.borg_repositories.update_borg_repository(
        borg_repository_update_request_factory.build(), id_=faker.pyint()
    )


def test_read_borg_repository(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.borg_repositories.read_borg_repository(id_=faker.pyint())


def test_delete_borg_repository(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.borg_repositories.delete_borg_repository(id_=faker.pyint())


def test_prune_borg_repository(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.borg_repositories.prune_borg_repository(id_=faker.pyint())


def test_check_borg_repository(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.borg_repositories.check_borg_repository(id_=faker.pyint())


def test_get_borg_archives_metadata(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.borg_repositories.get_borg_archives_metadata(id_=faker.pyint())


def test_list_borg_repositories(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.borg_repositories.list_borg_repositories()
