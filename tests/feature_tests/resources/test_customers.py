from cyberfusion.CoreApiClient.connector import CoreApiConnector
from tests.conftest import CustomerIPAddressCreateRequestFactory
import faker


def test_create_ip_address_for_customer(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    customer_ip_address_create_request_factory: CustomerIPAddressCreateRequestFactory,
) -> None:
    api_connector.customers.create_ip_address_for_customer(
        customer_ip_address_create_request_factory.build(), id_=faker.pyint()
    )


def test_read_customer(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.customers.read_customer(id_=faker.pyint())


def test_delete_ip_address_for_customer(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.customers.delete_ip_address_for_customer(
        id_=faker.pyint(), ip_address=faker.ipv6()
    )


def test_get_ip_addresses_products_for_customers(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.customers.get_ip_addresses_products_for_customers()


def test_list_customers(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.customers.list_customers()


def test_list_ip_addresses_for_customer(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.customers.list_ip_addresses_for_customer(id_=faker.pyint())
