from cyberfusion.CoreApiClient.connector import CoreApiConnector
from tests.conftest import (
    BasicAuthenticationRealmUpdateRequestFactory,
    BasicAuthenticationRealmCreateRequestFactory,
)
import faker


def test_create_basic_authentication_realm(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    basic_authentication_realm_create_request_factory: BasicAuthenticationRealmCreateRequestFactory,
) -> None:
    api_connector.basic_authentication_realms.create_basic_authentication_realm(
        basic_authentication_realm_create_request_factory.build()
    )


def test_update_basic_authentication_realm(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    basic_authentication_realm_update_request_factory: BasicAuthenticationRealmUpdateRequestFactory,
) -> None:
    api_connector.basic_authentication_realms.update_basic_authentication_realm(
        basic_authentication_realm_update_request_factory.build(), id_=faker.pyint()
    )


def test_read_basic_authentication_realm(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.basic_authentication_realms.read_basic_authentication_realm(
        id_=faker.pyint()
    )


def test_delete_basic_authentication_realm(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.basic_authentication_realms.delete_basic_authentication_realm(
        id_=faker.pyint()
    )


def test_list_basic_authentication_realms(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.basic_authentication_realms.list_basic_authentication_realms()
