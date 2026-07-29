from cyberfusion.CoreApiClient.connector import CoreApiConnector
from tests.conftest import ScheduledActionUpdateRequestFactory
import faker


def test_list_scheduled_actions(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.scheduled_actions.list_scheduled_actions()


def test_read_scheduled_action(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.scheduled_actions.read_scheduled_action(id_=faker.pyint())


def test_update_scheduled_action(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    scheduled_action_update_request_factory: ScheduledActionUpdateRequestFactory,
) -> None:
    api_connector.scheduled_actions.update_scheduled_action(
        scheduled_action_update_request_factory.build(), id_=faker.pyint()
    )


def test_delete_scheduled_action(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.scheduled_actions.delete_scheduled_action(id_=faker.pyint())
