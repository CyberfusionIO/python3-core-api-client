import random

from cyberfusion.CoreApiClient.connector import CoreApiConnector
from cyberfusion.CoreApiClient.models import NodeGroupEnum

from tests.conftest import NodeUpdateRequestFactory, NodeCreateRequestFactory
import faker


def test_create_nodes(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    node_create_request_factory: NodeCreateRequestFactory,
) -> None:
    api_connector.nodes.create_nodes(node_create_request_factory.build())


def test_update_node(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    node_update_request_factory: NodeUpdateRequestFactory,
) -> None:
    api_connector.nodes.update_node(
        node_update_request_factory.build(), id_=faker.pyint()
    )


def test_get_node_products(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.nodes.get_node_products()


def test_read_node(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.nodes.read_node(id_=faker.pyint())


def test_delete_node(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.nodes.delete_node(id_=faker.pyint())


def test_upgrade_downgrade_node(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    node_create_request_factory: NodeCreateRequestFactory,
) -> None:
    api_connector.nodes.upgrade_downgrade_node(
        id_=faker.pyint(), product=node_create_request_factory.build().product
    )


def test_list_nodes(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.nodes.list_nodes()


def test_add_node_groups(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.nodes.add_node_groups(
        id_=faker.pyint(), groups=[random.choice(list(NodeGroupEnum))]
    )
