from cyberfusion.CoreApiClient.connector import CoreApiConnector
from tests.conftest import (
    RedisInstanceUpdateRequestFactory,
    RedisInstanceCreateRequestFactory,
)
import faker


def test_create_redis_instance(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    redis_instance_create_request_factory: RedisInstanceCreateRequestFactory,
) -> None:
    api_connector.redis_instances.create_redis_instance(
        redis_instance_create_request_factory.build()
    )


def test_update_redis_instance(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    redis_instance_update_request_factory: RedisInstanceUpdateRequestFactory,
) -> None:
    api_connector.redis_instances.update_redis_instance(
        redis_instance_update_request_factory.build(), id_=faker.pyint()
    )


def test_read_redis_instance(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.redis_instances.read_redis_instance(id_=faker.pyint())


def test_delete_redis_instance(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.redis_instances.delete_redis_instance(id_=faker.pyint())


def test_list_redis_instances(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.redis_instances.list_redis_instances()
