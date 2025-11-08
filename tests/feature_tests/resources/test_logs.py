from cyberfusion.CoreApiClient.connector import CoreApiConnector
import faker


def test_list_object_logs(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.logs.list_object_logs()


def test_list_request_logs(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.logs.list_request_logs()
