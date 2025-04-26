from cyberfusion.CoreApiClient.connector import CoreApiConnector
from tests.conftest import (
    SshKeyCreatePrivateRequestFactory,
    SshKeyCreatePublicRequestFactory,
)
import faker


def test_create_public_ssh_key(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    ssh_key_create_public_request_factory: SshKeyCreatePublicRequestFactory,
) -> None:
    api_connector.ssh_keys.create_public_ssh_key(
        ssh_key_create_public_request_factory.build()
    )


def test_create_private_ssh_key(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    ssh_key_create_private_request_factory: SshKeyCreatePrivateRequestFactory,
) -> None:
    api_connector.ssh_keys.create_private_ssh_key(
        ssh_key_create_private_request_factory.build()
    )


def test_read_ssh_key(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.ssh_keys.read_ssh_key(id_=faker.pyint())


def test_delete_ssh_key(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.ssh_keys.delete_ssh_key(id_=faker.pyint())


def test_list_ssh_keys(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.ssh_keys.list_ssh_keys()
