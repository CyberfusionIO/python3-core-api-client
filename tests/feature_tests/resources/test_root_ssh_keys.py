from cyberfusion.CoreApiClient.connector import CoreApiConnector
from tests.conftest import (
    RootSshKeyCreatePrivateRequestFactory,
    RootSshKeyCreatePublicRequestFactory,
)
import faker


def test_create_public_root_ssh_key(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    root_ssh_key_create_public_request_factory: RootSshKeyCreatePublicRequestFactory,
) -> None:
    api_connector.root_ssh_keys.create_public_root_ssh_key(
        root_ssh_key_create_public_request_factory.build()
    )


def test_create_private_root_ssh_key(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    root_ssh_key_create_private_request_factory: RootSshKeyCreatePrivateRequestFactory,
) -> None:
    api_connector.root_ssh_keys.create_private_root_ssh_key(
        root_ssh_key_create_private_request_factory.build()
    )


def test_read_root_ssh_key(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.root_ssh_keys.read_root_ssh_key(id_=faker.pyint())


def test_delete_root_ssh_key(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.root_ssh_keys.delete_root_ssh_key(id_=faker.pyint())


def test_list_root_ssh_keys(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.root_ssh_keys.list_root_ssh_keys()
