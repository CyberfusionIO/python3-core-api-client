from cyberfusion.CoreApiClient.connector import CoreApiConnector
from tests.conftest import HaproxyListenCreateRequestFactory
import faker


def test_create_haproxy_listen(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    haproxy_listen_create_request_factory: HaproxyListenCreateRequestFactory,
) -> None:
    api_connector.haproxy_listens.create_haproxy_listen(
        haproxy_listen_create_request_factory.build()
    )


def test_list_haproxy_listens(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.haproxy_listens.list_haproxy_listens()


def test_read_haproxy_listen(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.haproxy_listens.read_haproxy_listen(id_=faker.pyint())


def test_delete_haproxy_listen(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.haproxy_listens.delete_haproxy_listen(id_=faker.pyint())
