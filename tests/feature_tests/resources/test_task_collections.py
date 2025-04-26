from cyberfusion.CoreApiClient.connector import CoreApiConnector
import faker


def test_retry_task_collection(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.task_collections.retry_task_collection(uuid=faker.uuid4())


def test_list_task_collection_results(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.task_collections.list_task_collection_results(uuid=faker.uuid4())
