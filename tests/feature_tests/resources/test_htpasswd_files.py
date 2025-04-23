from cyberfusion.CoreApiClient.connector import CoreApiConnector
from tests.conftest import HtpasswdFileCreateRequestFactory
import faker


def test_create_htpasswd_file(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    htpasswd_file_create_request_factory: HtpasswdFileCreateRequestFactory,
) -> None:
    api_connector.htpasswd_files.create_htpasswd_file(
        htpasswd_file_create_request_factory.build()
    )


def test_read_htpasswd_file(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.htpasswd_files.read_htpasswd_file(id_=faker.pyint())


def test_delete_htpasswd_file(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.htpasswd_files.delete_htpasswd_file(id_=faker.pyint())


def test_list_htpasswd_files(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.htpasswd_files.list_htpasswd_files()
