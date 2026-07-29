from cyberfusion.CoreApiClient.connector import CoreApiConnector
import faker


def test_read_health_check(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.health_checks.read_health_check(id_=faker.pyint())
