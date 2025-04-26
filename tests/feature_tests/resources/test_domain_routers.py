from cyberfusion.CoreApiClient.connector import CoreApiConnector
from tests.conftest import DomainRouterUpdateRequestFactory
import faker


def test_update_domain_router(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    domain_router_update_request_factory: DomainRouterUpdateRequestFactory,
) -> None:
    api_connector.domain_routers.update_domain_router(
        domain_router_update_request_factory.build(), id_=faker.pyint()
    )


def test_list_domain_routers(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.domain_routers.list_domain_routers()
