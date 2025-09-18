from cyberfusion.CoreApiClient.connector import CoreApiConnector
from tests.conftest import (
    ClusterIPAddressCreateRequestFactory,
    ClusterUpdateRequestFactory,
    ClusterCreateRequestFactory,
    ClusterBorgPropertiesCreateRequestFactory,
    ClusterElasticsearchPropertiesCreateRequestFactory,
    ClusterFirewallPropertiesCreateRequestFactory,
    ClusterGrafanaPropertiesCreateRequestFactory,
    ClusterKernelcarePropertiesCreateRequestFactory,
    ClusterLoadBalancingPropertiesCreateRequestFactory,
    ClusterMariadbPropertiesCreateRequestFactory,
    ClusterMeilisearchPropertiesCreateRequestFactory,
    ClusterMetabasePropertiesCreateRequestFactory,
    ClusterNewRelicPropertiesCreateRequestFactory,
    ClusterNodejsPropertiesCreateRequestFactory,
    ClusterOsPropertiesCreateRequestFactory,
    ClusterPhpPropertiesCreateRequestFactory,
    ClusterPostgresqlPropertiesCreateRequestFactory,
    ClusterRabbitmqPropertiesCreateRequestFactory,
    ClusterSinglestorePropertiesCreateRequestFactory,
    ClusterUnixUsersPropertiesCreateRequestFactory,
    ClusterRabbitmqPropertiesUpdateRequestFactory,
    ClusterBorgPropertiesUpdateRequestFactory,
    ClusterElasticsearchPropertiesUpdateRequestFactory,
    ClusterFirewallPropertiesUpdateRequestFactory,
    ClusterGrafanaPropertiesUpdateRequestFactory,
    ClusterKernelcarePropertiesUpdateRequestFactory,
    ClusterLoadBalancingPropertiesUpdateRequestFactory,
    ClusterMariadbPropertiesUpdateRequestFactory,
    ClusterMeilisearchPropertiesUpdateRequestFactory,
    ClusterMetabasePropertiesUpdateRequestFactory,
    ClusterNewRelicPropertiesUpdateRequestFactory,
    ClusterNodejsPropertiesUpdateRequestFactory,
    ClusterOsPropertiesUpdateRequestFactory,
    ClusterPhpPropertiesUpdateRequestFactory,
    ClusterPostgresqlPropertiesUpdateRequestFactory,
)
import faker


def test_create_cluster(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    cluster_create_request_factory: ClusterCreateRequestFactory,
) -> None:
    api_connector.clusters.create_cluster(cluster_create_request_factory.build())


def test_create_borg_properties(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    cluster_borg_properties_create_request_factory: ClusterBorgPropertiesCreateRequestFactory,
) -> None:
    api_connector.clusters.create_borg_properties(
        cluster_borg_properties_create_request_factory.build(), id_=faker.pyint()
    )


def test_create_elasticsearch_properties(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    cluster_elasticsearch_properties_create_request_factory: ClusterElasticsearchPropertiesCreateRequestFactory,
) -> None:
    api_connector.clusters.create_elasticsearch_properties(
        cluster_elasticsearch_properties_create_request_factory.build(),
        id_=faker.pyint(),
    )


def test_create_firewall_properties(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    cluster_firewall_properties_create_request_factory: ClusterFirewallPropertiesCreateRequestFactory,
) -> None:
    api_connector.clusters.create_firewall_properties(
        cluster_firewall_properties_create_request_factory.build(), id_=faker.pyint()
    )


def test_create_grafana_properties(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    cluster_grafana_properties_create_request_factory: ClusterGrafanaPropertiesCreateRequestFactory,
) -> None:
    api_connector.clusters.create_grafana_properties(
        cluster_grafana_properties_create_request_factory.build(), id_=faker.pyint()
    )


def test_create_kernelcare_properties(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    cluster_kernelcare_properties_create_request_factory: ClusterKernelcarePropertiesCreateRequestFactory,
) -> None:
    api_connector.clusters.create_kernelcare_properties(
        cluster_kernelcare_properties_create_request_factory.build(), id_=faker.pyint()
    )


def test_create_load_balancing_properties(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    cluster_load_balancing_properties_create_request_factory: ClusterLoadBalancingPropertiesCreateRequestFactory,
) -> None:
    api_connector.clusters.create_load_balancing_properties(
        cluster_load_balancing_properties_create_request_factory.build(),
        id_=faker.pyint(),
    )


def test_create_mariadb_properties(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    cluster_mariadb_properties_create_request_factory: ClusterMariadbPropertiesCreateRequestFactory,
) -> None:
    api_connector.clusters.create_mariadb_properties(
        cluster_mariadb_properties_create_request_factory.build(), id_=faker.pyint()
    )


def test_create_meilisearch_properties(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    cluster_meilisearch_properties_create_request_factory: ClusterMeilisearchPropertiesCreateRequestFactory,
) -> None:
    api_connector.clusters.create_meilisearch_properties(
        cluster_meilisearch_properties_create_request_factory.build(), id_=faker.pyint()
    )


def test_create_metabase_properties(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    cluster_metabase_properties_create_request_factory: ClusterMetabasePropertiesCreateRequestFactory,
) -> None:
    api_connector.clusters.create_metabase_properties(
        cluster_metabase_properties_create_request_factory.build(), id_=faker.pyint()
    )


def test_create_new_relic_properties(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    cluster_new_relic_properties_create_request_factory: ClusterNewRelicPropertiesCreateRequestFactory,
) -> None:
    api_connector.clusters.create_new_relic_properties(
        cluster_new_relic_properties_create_request_factory.build(), id_=faker.pyint()
    )


def test_create_nodejs_properties(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    cluster_nodejs_properties_create_request_factory: ClusterNodejsPropertiesCreateRequestFactory,
) -> None:
    api_connector.clusters.create_nodejs_properties(
        cluster_nodejs_properties_create_request_factory.build(), id_=faker.pyint()
    )


def test_create_os_properties(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    cluster_os_properties_create_request_factory: ClusterOsPropertiesCreateRequestFactory,
) -> None:
    api_connector.clusters.create_os_properties(
        cluster_os_properties_create_request_factory.build(), id_=faker.pyint()
    )


def test_create_php_properties(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    cluster_php_properties_create_request_factory: ClusterPhpPropertiesCreateRequestFactory,
) -> None:
    api_connector.clusters.create_php_properties(
        cluster_php_properties_create_request_factory.build(), id_=faker.pyint()
    )


def test_create_postgresql_properties(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    cluster_postgresql_properties_create_request_factory: ClusterPostgresqlPropertiesCreateRequestFactory,
) -> None:
    api_connector.clusters.create_postgresql_properties(
        cluster_postgresql_properties_create_request_factory.build(), id_=faker.pyint()
    )


def test_create_rabbitmq_properties(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    cluster_rabbitmq_properties_create_request_factory: ClusterRabbitmqPropertiesCreateRequestFactory,
) -> None:
    api_connector.clusters.create_rabbitmq_properties(
        cluster_rabbitmq_properties_create_request_factory.build(), id_=faker.pyint()
    )


def test_create_singlestore_properties(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    cluster_singlestore_properties_create_request_factory: ClusterSinglestorePropertiesCreateRequestFactory,
) -> None:
    api_connector.clusters.create_singlestore_properties(
        cluster_singlestore_properties_create_request_factory.build(), id_=faker.pyint()
    )


def test_create_unix_users_properties(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    cluster_unix_users_properties_create_request_factory: ClusterUnixUsersPropertiesCreateRequestFactory,
) -> None:
    api_connector.clusters.create_unix_users_properties(
        cluster_unix_users_properties_create_request_factory.build(), id_=faker.pyint()
    )


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


def test_get_nodes_specifications(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.clusters.get_nodes_specifications(id_=faker.pyint())


def test_list_simple_specifications(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.clusters.list_simple_specifications(id_=faker.pyint())


def test_list_advanced_specifications(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.clusters.list_advanced_specifications(id_=faker.pyint())


def test_read_borg_properties(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.clusters.read_borg_properties(id_=faker.pyint())


def test_read_elasticsearch_properties(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.clusters.read_elasticsearch_properties(id_=faker.pyint())


def test_read_firewall_properties(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.clusters.read_firewall_properties(id_=faker.pyint())


def test_read_grafana_properties(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.clusters.read_grafana_properties(id_=faker.pyint())


def test_read_kernelcare_properties(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.clusters.read_kernelcare_properties(id_=faker.pyint())


def test_read_load_balancing_properties(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.clusters.read_load_balancing_properties(id_=faker.pyint())


def test_read_mariadb_properties(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.clusters.read_mariadb_properties(id_=faker.pyint())


def test_read_meilisearch_properties(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.clusters.read_meilisearch_properties(id_=faker.pyint())


def test_read_metabase_properties(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.clusters.read_metabase_properties(id_=faker.pyint())


def test_read_new_relic_properties(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.clusters.read_new_relic_properties(id_=faker.pyint())


def test_read_nodejs_properties(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.clusters.read_nodejs_properties(id_=faker.pyint())


def test_read_os_properties(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.clusters.read_os_properties(id_=faker.pyint())


def test_read_php_properties(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.clusters.read_php_properties(id_=faker.pyint())


def test_read_postgresql_properties(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.clusters.read_postgresql_properties(id_=faker.pyint())


def test_read_rabbitmq_properties(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.clusters.read_rabbitmq_properties(id_=faker.pyint())


def test_read_redis_properties(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.clusters.read_redis_properties(id_=faker.pyint())


def test_read_singlestore_properties(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.clusters.read_singlestore_properties(id_=faker.pyint())


def test_read_unix_users_properties(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.clusters.read_unix_users_properties(id_=faker.pyint())


def test_list_borg_properties(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.clusters.list_borg_properties(id_=faker.pyint())


def test_list_redis_properties(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.clusters.list_redis_properties(id_=faker.pyint())


def test_list_elasticsearch_properties(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.clusters.list_elasticsearch_properties(id_=faker.pyint())


def test_list_firewall_properties(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.clusters.list_firewall_properties(id_=faker.pyint())


def test_list_grafana_properties(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.clusters.list_grafana_properties(id_=faker.pyint())


def test_list_kernelcare_properties(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.clusters.list_kernelcare_properties(id_=faker.pyint())


def test_list_load_balancing_properties(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.clusters.list_load_balancing_properties(id_=faker.pyint())


def test_list_mariadb_properties(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.clusters.list_mariadb_properties(id_=faker.pyint())


def test_list_meilisearch_properties(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.clusters.list_meilisearch_properties(id_=faker.pyint())


def test_list_metabase_properties(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.clusters.list_metabase_properties(id_=faker.pyint())


def test_list_new_relic_properties(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.clusters.list_new_relic_properties(id_=faker.pyint())


def test_list_nodejs_properties(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.clusters.list_nodejs_properties(id_=faker.pyint())


def test_list_os_properties(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.clusters.list_os_properties(id_=faker.pyint())


def test_list_php_properties(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.clusters.list_php_properties(id_=faker.pyint())


def test_list_postgresql_properties(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.clusters.list_postgresql_properties(id_=faker.pyint())


def test_list_rabbitmq_properties(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.clusters.list_rabbitmq_properties(id_=faker.pyint())


def test_list_singlestore_properties(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.clusters.list_singlestore_properties(id_=faker.pyint())


def test_list_unix_users_properties(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.clusters.list_unix_users_properties(id_=faker.pyint())


def test_update_borg_properties(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    cluster_borg_properties_update_request_factory: ClusterBorgPropertiesUpdateRequestFactory,
) -> None:
    api_connector.clusters.update_borg_properties(
        cluster_borg_properties_update_request_factory.build(), id_=faker.pyint()
    )


def test_update_elasticsearch_properties(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    cluster_elasticsearch_properties_update_request_factory: ClusterElasticsearchPropertiesUpdateRequestFactory,
) -> None:
    api_connector.clusters.update_elasticsearch_properties(
        cluster_elasticsearch_properties_update_request_factory.build(),
        id_=faker.pyint(),
    )


def test_update_firewall_properties(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    cluster_firewall_properties_update_request_factory: ClusterFirewallPropertiesUpdateRequestFactory,
) -> None:
    api_connector.clusters.update_firewall_properties(
        cluster_firewall_properties_update_request_factory.build(), id_=faker.pyint()
    )


def test_update_grafana_properties(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    cluster_grafana_properties_update_request_factory: ClusterGrafanaPropertiesUpdateRequestFactory,
) -> None:
    api_connector.clusters.update_grafana_properties(
        cluster_grafana_properties_update_request_factory.build(), id_=faker.pyint()
    )


def test_update_kernelcare_properties(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    cluster_kernelcare_properties_update_request_factory: ClusterKernelcarePropertiesUpdateRequestFactory,
) -> None:
    api_connector.clusters.update_kernelcare_properties(
        cluster_kernelcare_properties_update_request_factory.build(), id_=faker.pyint()
    )


def test_update_load_balancing_properties(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    cluster_load_balancing_properties_update_request_factory: ClusterLoadBalancingPropertiesUpdateRequestFactory,
) -> None:
    api_connector.clusters.update_load_balancing_properties(
        cluster_load_balancing_properties_update_request_factory.build(),
        id_=faker.pyint(),
    )


def test_update_mariadb_properties(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    cluster_mariadb_properties_update_request_factory: ClusterMariadbPropertiesUpdateRequestFactory,
) -> None:
    api_connector.clusters.update_mariadb_properties(
        cluster_mariadb_properties_update_request_factory.build(), id_=faker.pyint()
    )


def test_update_meilisearch_properties(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    cluster_meilisearch_properties_update_request_factory: ClusterMeilisearchPropertiesUpdateRequestFactory,
) -> None:
    api_connector.clusters.update_meilisearch_properties(
        cluster_meilisearch_properties_update_request_factory.build(), id_=faker.pyint()
    )


def test_update_metabase_properties(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    cluster_metabase_properties_update_request_factory: ClusterMetabasePropertiesUpdateRequestFactory,
) -> None:
    api_connector.clusters.update_metabase_properties(
        cluster_metabase_properties_update_request_factory.build(), id_=faker.pyint()
    )


def test_update_new_relic_properties(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    cluster_new_relic_properties_update_request_factory: ClusterNewRelicPropertiesUpdateRequestFactory,
) -> None:
    api_connector.clusters.update_new_relic_properties(
        cluster_new_relic_properties_update_request_factory.build(), id_=faker.pyint()
    )


def test_update_nodejs_properties(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    cluster_nodejs_properties_update_request_factory: ClusterNodejsPropertiesUpdateRequestFactory,
) -> None:
    api_connector.clusters.update_nodejs_properties(
        cluster_nodejs_properties_update_request_factory.build(), id_=faker.pyint()
    )


def test_update_os_properties(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    cluster_os_properties_update_request_factory: ClusterOsPropertiesUpdateRequestFactory,
) -> None:
    api_connector.clusters.update_os_properties(
        cluster_os_properties_update_request_factory.build(), id_=faker.pyint()
    )


def test_update_php_properties(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    cluster_php_properties_update_request_factory: ClusterPhpPropertiesUpdateRequestFactory,
) -> None:
    api_connector.clusters.update_php_properties(
        cluster_php_properties_update_request_factory.build(), id_=faker.pyint()
    )


def test_update_postgresql_properties(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    cluster_postgresql_properties_update_request_factory: ClusterPostgresqlPropertiesUpdateRequestFactory,
) -> None:
    api_connector.clusters.update_postgresql_properties(
        cluster_postgresql_properties_update_request_factory.build(), id_=faker.pyint()
    )


def test_update_rabbitmq_properties(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    cluster_rabbitmq_properties_update_request_factory: ClusterRabbitmqPropertiesUpdateRequestFactory,
) -> None:
    api_connector.clusters.update_rabbitmq_properties(
        cluster_rabbitmq_properties_update_request_factory.build(), id_=faker.pyint()
    )
