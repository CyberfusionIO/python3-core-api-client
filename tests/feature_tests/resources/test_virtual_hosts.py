from cyberfusion.CoreApiClient.connector import CoreApiConnector
from tests.conftest import (
    VirtualHostUpdateRequestFactory,
    VirtualHostCreateRequestFactory,
)
import faker


def test_create_virtual_host(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    virtual_host_create_request_factory: VirtualHostCreateRequestFactory,
) -> None:
    api_connector.virtual_hosts.create_virtual_host(
        virtual_host_create_request_factory.build()
    )


def test_update_virtual_host(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    virtual_host_update_request_factory: VirtualHostUpdateRequestFactory,
) -> None:
    api_connector.virtual_hosts.update_virtual_host(
        virtual_host_update_request_factory.build(), id_=faker.pyint()
    )


def test_read_virtual_host(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.virtual_hosts.read_virtual_host(id_=faker.pyint())


def test_delete_virtual_host(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.virtual_hosts.delete_virtual_host(id_=faker.pyint())


def test_get_virtual_host_document_root(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.virtual_hosts.get_virtual_host_document_root(id_=faker.pyint())


def test_sync_domain_roots_of_virtual_hosts(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.virtual_hosts.sync_domain_roots_of_virtual_hosts(
        left_virtual_host_id=faker.pyint(), right_virtual_host_id=faker.pyint()
    )


def test_list_virtual_hosts(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.virtual_hosts.list_virtual_hosts()


def test_list_access_logs(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.virtual_hosts.list_access_logs(id_=faker.pyint())


def test_list_error_logs(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.virtual_hosts.list_error_logs(id_=faker.pyint())
