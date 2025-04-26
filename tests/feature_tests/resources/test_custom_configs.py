from cyberfusion.CoreApiClient.connector import CoreApiConnector
from tests.conftest import (
    CustomConfigUpdateRequestFactory,
    CustomConfigCreateRequestFactory,
)
import faker


def test_create_custom_config(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    custom_config_create_request_factory: CustomConfigCreateRequestFactory,
) -> None:
    api_connector.custom_configs.create_custom_config(
        custom_config_create_request_factory.build()
    )


def test_update_custom_config(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    custom_config_update_request_factory: CustomConfigUpdateRequestFactory,
) -> None:
    api_connector.custom_configs.update_custom_config(
        custom_config_update_request_factory.build(), id_=faker.pyint()
    )


def test_read_custom_config(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.custom_configs.read_custom_config(id_=faker.pyint())


def test_delete_custom_config(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.custom_configs.delete_custom_config(id_=faker.pyint())


def test_list_custom_configs(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.custom_configs.list_custom_configs()
