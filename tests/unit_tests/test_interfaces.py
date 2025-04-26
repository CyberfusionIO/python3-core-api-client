from cyberfusion.CoreApiClient.connector import CoreApiConnector
from cyberfusion.CoreApiClient.interfaces import Resource


def test_api_connector_attribute(api_connector: CoreApiConnector) -> None:
    resource = Resource(api_connector)

    assert resource.api_connector == api_connector
