from cyberfusion.CoreApiClient.connector import CoreApiConnector
from tests.conftest import FirewallRuleCreateRequestFactory
import faker


def test_create_firewall_rule(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    firewall_rule_create_request_factory: FirewallRuleCreateRequestFactory,
) -> None:
    api_connector.firewall_rules.create_firewall_rule(
        firewall_rule_create_request_factory.build()
    )


def test_read_firewall_rule(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.firewall_rules.read_firewall_rule(id_=faker.pyint())


def test_delete_firewall_rule(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.firewall_rules.delete_firewall_rule(id_=faker.pyint())


def test_list_firewall_rules(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.firewall_rules.list_firewall_rules()
