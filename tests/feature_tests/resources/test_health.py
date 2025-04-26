from cyberfusion.CoreApiClient.connector import CoreApiConnector
import faker


def test_read_health(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.health.read_health()
