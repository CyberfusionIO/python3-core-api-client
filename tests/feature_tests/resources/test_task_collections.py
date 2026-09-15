from cyberfusion.CoreApiClient.connector import CoreApiConnector
import faker


def test_list_task_collection_results(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.task_collections.list_task_collection_results(uuid=faker.uuid4())
