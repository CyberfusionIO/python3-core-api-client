from cyberfusion.CoreApiClient.connector import CoreApiConnector
from tests.conftest import DaemonUpdateRequestFactory, DaemonCreateRequestFactory
import faker


def test_create_daemon(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    daemon_create_request_factory: DaemonCreateRequestFactory,
) -> None:
    api_connector.daemons.create_daemon(daemon_create_request_factory.build())


def test_update_daemon(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    daemon_update_request_factory: DaemonUpdateRequestFactory,
) -> None:
    api_connector.daemons.update_daemon(
        daemon_update_request_factory.build(), id_=faker.pyint()
    )


def test_read_daemon(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.daemons.read_daemon(id_=faker.pyint())


def test_delete_daemon(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.daemons.delete_daemon(id_=faker.pyint())


def test_list_daemons(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.daemons.list_daemons()
