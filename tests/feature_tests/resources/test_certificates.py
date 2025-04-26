from cyberfusion.CoreApiClient.connector import CoreApiConnector
from tests.conftest import CertificateCreateRequestFactory
import faker


def test_create_certificate(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    certificate_create_request_factory: CertificateCreateRequestFactory,
) -> None:
    api_connector.certificates.create_certificate(
        certificate_create_request_factory.build()
    )


def test_read_certificate(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.certificates.read_certificate(id_=faker.pyint())


def test_delete_certificate(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.certificates.delete_certificate(id_=faker.pyint())


def test_list_certificates(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.certificates.list_certificates()
