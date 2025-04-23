from cyberfusion.CoreApiClient.connector import CoreApiConnector
from tests.conftest import (
    SecurityTxtPolicyUpdateRequestFactory,
    SecurityTxtPolicyCreateRequestFactory,
)
import faker


def test_create_security_txt_policy(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    security_txt_policy_create_request_factory: SecurityTxtPolicyCreateRequestFactory,
) -> None:
    api_connector.security_txt_policies.create_security_txt_policy(
        security_txt_policy_create_request_factory.build()
    )


def test_update_security_txt_policy(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    security_txt_policy_update_request_factory: SecurityTxtPolicyUpdateRequestFactory,
) -> None:
    api_connector.security_txt_policies.update_security_txt_policy(
        security_txt_policy_update_request_factory.build(), id_=faker.pyint()
    )


def test_read_security_txt_policy(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.security_txt_policies.read_security_txt_policy(id_=faker.pyint())


def test_delete_security_txt_policy(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.security_txt_policies.delete_security_txt_policy(id_=faker.pyint())


def test_list_security_txt_policies(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.security_txt_policies.list_security_txt_policies()
