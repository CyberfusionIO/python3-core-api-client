from cyberfusion.CoreApiClient.connector import CoreApiConnector
import faker


def test_list_regions(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.regions.list_regions()
