from cyberfusion.CoreApiClient.connector import CoreApiConnector
from tests.conftest import (
    FirewallGroupUpdateRequestFactory,
    FirewallGroupCreateRequestFactory,
)
import faker


def test_create_firewall_group(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    firewall_group_create_request_factory: FirewallGroupCreateRequestFactory,
) -> None:
    api_connector.firewall_groups.create_firewall_group(
        firewall_group_create_request_factory.build()
    )


def test_update_firewall_group(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    firewall_group_update_request_factory: FirewallGroupUpdateRequestFactory,
) -> None:
    api_connector.firewall_groups.update_firewall_group(
        firewall_group_update_request_factory.build(), id_=faker.pyint()
    )


def test_read_firewall_group(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.firewall_groups.read_firewall_group(id_=faker.pyint())


def test_delete_firewall_group(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.firewall_groups.delete_firewall_group(id_=faker.pyint())


def test_list_firewall_groups(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.firewall_groups.list_firewall_groups()
