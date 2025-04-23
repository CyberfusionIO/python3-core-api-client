from cyberfusion.CoreApiClient.connector import CoreApiConnector
from tests.conftest import CronUpdateRequestFactory, CronCreateRequestFactory
import faker


def test_create_cron(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    cron_create_request_factory: CronCreateRequestFactory,
) -> None:
    api_connector.crons.create_cron(cron_create_request_factory.build())


def test_update_cron(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    cron_update_request_factory: CronUpdateRequestFactory,
) -> None:
    api_connector.crons.update_cron(
        cron_update_request_factory.build(), id_=faker.pyint()
    )


def test_read_cron(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.crons.read_cron(id_=faker.pyint())


def test_delete_cron(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.crons.delete_cron(id_=faker.pyint())


def test_list_crons(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.crons.list_crons()
