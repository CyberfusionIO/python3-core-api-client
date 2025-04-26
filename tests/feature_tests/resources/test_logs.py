from cyberfusion.CoreApiClient.connector import CoreApiConnector
import faker


def test_list_access_logs(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.logs.list_access_logs(virtual_host_id=faker.pyint())


def test_list_error_logs(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.logs.list_error_logs(virtual_host_id=faker.pyint())
