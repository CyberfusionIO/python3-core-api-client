from cyberfusion.CoreApiClient.connector import CoreApiConnector
from tests.conftest import HostsEntryCreateRequestFactory
import faker


def test_create_hosts_entry(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    hosts_entry_create_request_factory: HostsEntryCreateRequestFactory,
) -> None:
    api_connector.hosts_entries.create_hosts_entry(
        hosts_entry_create_request_factory.build()
    )


def test_read_hosts_entry(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.hosts_entries.read_hosts_entry(id_=faker.pyint())


def test_delete_hosts_entry(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.hosts_entries.delete_hosts_entry(id_=faker.pyint())


def test_list_hosts_entries(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.hosts_entries.list_hosts_entries()
