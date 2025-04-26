from cyberfusion.CoreApiClient.connector import CoreApiConnector
from tests.conftest import (
    URLRedirectUpdateRequestFactory,
    URLRedirectCreateRequestFactory,
)
import faker


def test_create_url_redirect(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    url_redirect_create_request_factory: URLRedirectCreateRequestFactory,
) -> None:
    api_connector.url_redirects.create_url_redirect(
        url_redirect_create_request_factory.build()
    )


def test_update_url_redirect(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    url_redirect_update_request_factory: URLRedirectUpdateRequestFactory,
) -> None:
    api_connector.url_redirects.update_url_redirect(
        url_redirect_update_request_factory.build(), id_=faker.pyint()
    )


def test_read_url_redirect(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.url_redirects.read_url_redirect(id_=faker.pyint())


def test_delete_url_redirect(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.url_redirects.delete_url_redirect(id_=faker.pyint())


def test_list_url_redirects(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.url_redirects.list_url_redirects()
