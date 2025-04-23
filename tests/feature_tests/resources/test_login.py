from cyberfusion.CoreApiClient.connector import CoreApiConnector
from tests.conftest import BodyLoginAccessTokenFactory
import faker


def test_request_access_token(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    body_login_access_token_factory: BodyLoginAccessTokenFactory,
) -> None:
    api_connector.login.request_access_token(body_login_access_token_factory.build())


def test_test_access_token(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.login.test_access_token()
