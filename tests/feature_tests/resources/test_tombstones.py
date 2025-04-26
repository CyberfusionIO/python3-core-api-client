from cyberfusion.CoreApiClient.connector import CoreApiConnector
import faker


def test_list_tombstones(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.tombstones.list_tombstones()
