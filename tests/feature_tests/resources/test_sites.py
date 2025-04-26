from cyberfusion.CoreApiClient.connector import CoreApiConnector
import faker


def test_list_sites(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.sites.list_sites()
