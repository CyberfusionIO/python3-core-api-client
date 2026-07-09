from cyberfusion.CoreApiClient.connector import CoreApiConnector
from tests.conftest import (
    CarbonTxtCreateRequestFactory,
    CarbonTxtUpdateRequestFactory,
)
import faker


def test_create_carbon_txt_policy(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    carbon_txt_create_request_factory: CarbonTxtCreateRequestFactory,
) -> None:
    api_connector.carbon_txts.create_carbon_txt_policy(
        carbon_txt_create_request_factory.build()
    )


def test_update_carbon_txt_policy(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    carbon_txt_update_request_factory: CarbonTxtUpdateRequestFactory,
) -> None:
    api_connector.carbon_txts.update_carbon_txt_policy(
        carbon_txt_update_request_factory.build(), id_=faker.pyint()
    )


def test_read_carbon_txt_policy(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.carbon_txts.read_carbon_txt_policy(id_=faker.pyint())


def test_delete_carbon_txt_policy(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.carbon_txts.delete_carbon_txt_policy(id_=faker.pyint())


def test_list_carbon_txt_policies(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.carbon_txts.list_carbon_txt_policies()
