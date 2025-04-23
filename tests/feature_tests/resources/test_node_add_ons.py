from cyberfusion.CoreApiClient.connector import CoreApiConnector
from tests.conftest import NodeAddOnCreateRequestFactory
import faker


def test_create_node_add_on(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    node_add_on_create_request_factory: NodeAddOnCreateRequestFactory,
) -> None:
    api_connector.node_add_ons.create_node_add_on(
        node_add_on_create_request_factory.build()
    )


def test_get_node_add_on_products(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.node_add_ons.get_node_add_on_products()


def test_read_node_add_on(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.node_add_ons.read_node_add_on(id_=faker.pyint())


def test_delete_node_add_on(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.node_add_ons.delete_node_add_on(id_=faker.pyint())


def test_list_node_add_ons(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.node_add_ons.list_node_add_ons()
