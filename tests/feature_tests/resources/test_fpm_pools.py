from cyberfusion.CoreApiClient.connector import CoreApiConnector
from tests.conftest import FpmPoolUpdateRequestFactory, FpmPoolCreateRequestFactory
import faker


def test_create_fpm_pool(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    fpm_pool_create_request_factory: FpmPoolCreateRequestFactory,
) -> None:
    api_connector.fpm_pools.create_fpm_pool(fpm_pool_create_request_factory.build())


def test_update_fpm_pool(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    fpm_pool_update_request_factory: FpmPoolUpdateRequestFactory,
) -> None:
    api_connector.fpm_pools.update_fpm_pool(
        fpm_pool_update_request_factory.build(), id_=faker.pyint()
    )


def test_read_fpm_pool(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.fpm_pools.read_fpm_pool(id_=faker.pyint())


def test_delete_fpm_pool(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.fpm_pools.delete_fpm_pool(id_=faker.pyint())


def test_restart_fpm_pool(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.fpm_pools.restart_fpm_pool(id_=faker.pyint())


def test_reload_fpm_pool(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.fpm_pools.reload_fpm_pool(id_=faker.pyint())


def test_list_fpm_pools(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.fpm_pools.list_fpm_pools()


def test_get_fpm_pool_status(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.fpm_pools.get_fpm_pool_status(id_=faker.pyint())


def test_update_fpm_pool_version(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.fpm_pools.update_fpm_pool_version(
        id_=faker.pyint(), version=faker.pystr()
    )
