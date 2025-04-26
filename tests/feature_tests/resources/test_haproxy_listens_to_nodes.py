from cyberfusion.CoreApiClient.connector import CoreApiConnector
from tests.conftest import HaproxyListenToNodeCreateRequestFactory
import faker


def test_create_haproxy_listen_to_node(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    haproxy_listen_to_node_create_request_factory: HaproxyListenToNodeCreateRequestFactory,
) -> None:
    api_connector.haproxy_listens_to_nodes.create_haproxy_listen_to_node(
        haproxy_listen_to_node_create_request_factory.build()
    )


def test_list_haproxy_listens_to_nodes(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.haproxy_listens_to_nodes.list_haproxy_listens_to_nodes()


def test_read_haproxy_listen_to_node(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.haproxy_listens_to_nodes.read_haproxy_listen_to_node(
        id_=faker.pyint()
    )


def test_delete_haproxy_listen_to_node(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.haproxy_listens_to_nodes.delete_haproxy_listen_to_node(
        id_=faker.pyint()
    )
