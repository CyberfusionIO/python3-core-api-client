from cyberfusion.CoreApiClient.connector import CoreApiConnector
import faker


def test_list_available_nodejs_versions(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.available_versions.list_available_nodejs_versions()


def test_list_available_php_versions(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.available_versions.list_available_php_versions()


def test_list_available_wordpress_versions(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.available_versions.list_available_wordpress_versions()
