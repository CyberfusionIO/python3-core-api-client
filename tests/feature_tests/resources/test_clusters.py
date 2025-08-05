from cyberfusion.CoreApiClient.connector import CoreApiConnector
from tests.conftest import (
    ClusterIPAddressCreateRequestFactory,
    ClusterUpdateRequestFactory,
    ClusterCreateRequestFactory,
)
import faker


def test_create_cluster(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    cluster_create_request_factory: ClusterCreateRequestFactory,
) -> None:
    api_connector.clusters.create_cluster(cluster_create_request_factory.build())


def test_update_cluster(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    cluster_update_request_factory: ClusterUpdateRequestFactory,
) -> None:
    api_connector.clusters.update_cluster(
        cluster_update_request_factory.build(), id_=faker.pyint()
    )


def test_create_ip_address_for_cluster(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    cluster_ip_address_create_request_factory: ClusterIPAddressCreateRequestFactory,
) -> None:
    api_connector.clusters.create_ip_address_for_cluster(
        cluster_ip_address_create_request_factory.build(), id_=faker.pyint()
    )


def test_get_common_properties(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.clusters.get_common_properties()


def test_read_cluster(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.clusters.read_cluster(id_=faker.pyint())


def test_get_borg_ssh_key(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.clusters.get_borg_ssh_key(id_=faker.pyint())


def test_delete_ip_address_for_cluster(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.clusters.delete_ip_address_for_cluster(
        id_=faker.pyint(), ip_address=faker.ipv6()
    )


def test_enable_l3_ddos_protection_for_ip_address(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.clusters.enable_l3_ddos_protection_for_ip_address(
        id_=faker.pyint(), ip_address=faker.ipv6()
    )


def test_disable_l3_ddos_protection_for_ip_address(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.clusters.disable_l3_ddos_protection_for_ip_address(
        id_=faker.pyint(), ip_address=faker.ipv6()
    )


def test_get_ip_addresses_products_for_clusters(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.clusters.get_ip_addresses_products_for_clusters()


def test_list_clusters(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.clusters.list_clusters()


def test_list_ip_addresses_for_cluster(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.clusters.list_ip_addresses_for_cluster(id_=faker.pyint())


def test_list_cluster_deployments_results(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.clusters.list_cluster_deployments_results(id_=faker.pyint())


def test_list_unix_users_home_directory_usages(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.clusters.list_unix_users_home_directory_usages(
        cluster_id=faker.pyint(), timestamp=faker.date_time()
    )


def test_list_nodes_dependencies(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.clusters.list_nodes_dependencies(id_=faker.pyint())
