from cyberfusion.CoreApiClient.connector import CoreApiConnector
from tests.conftest import (
    N8nInstanceUpdateRequestFactory,
    N8nInstanceCreateRequestFactory,
)
import faker


def test_create_n8n_instance(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    n8n_instance_create_request_factory: N8nInstanceCreateRequestFactory,
) -> None:
    api_connector.n8n_instances.create_n8n_instance(
        n8n_instance_create_request_factory.build()
    )


def test_update_n8n_instance(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    n8n_instance_update_request_factory: N8nInstanceUpdateRequestFactory,
) -> None:
    api_connector.n8n_instances.update_n8n_instance(
        n8n_instance_update_request_factory.build(), id_=faker.pyint()
    )


def test_read_n8n_instance(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.n8n_instances.read_n8n_instance(id_=faker.pyint())


def test_delete_n8n_instance(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.n8n_instances.delete_n8n_instance(id_=faker.pyint())


def test_list_n8n_instances(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.n8n_instances.list_n8n_instances()
