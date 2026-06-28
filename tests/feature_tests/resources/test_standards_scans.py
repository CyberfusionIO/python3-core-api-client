from cyberfusion.CoreApiClient.connector import CoreApiConnector
import faker

from tests.conftest import StandardsScansSearchRequestFactory


def test_list_standards_scans(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.standards_scans.list_standards_scans()


def test_list_standards_scans_with_filters(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    standards_scans_search_request_factory: StandardsScansSearchRequestFactory,
) -> None:
    api_connector.standards_scans.list_standards_scans(
        include_filters=standards_scans_search_request_factory.build()
    )


def test_read_standards_scan(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.standards_scans.read_standards_scan(id_=faker.pyint())


def test_read_standards_scan_results(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.standards_scans.read_standards_scan_results(id_=faker.pyint())
