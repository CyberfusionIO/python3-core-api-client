from cyberfusion.CoreApiClient.connector import CoreApiConnector
from tests.conftest import (
    CertificateManagerUpdateRequestFactory,
    CertificateManagerCreateRequestFactory,
)
import faker


def test_create_certificate_manager(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    certificate_manager_create_request_factory: CertificateManagerCreateRequestFactory,
) -> None:
    api_connector.certificate_managers.create_certificate_manager(
        certificate_manager_create_request_factory.build()
    )


def test_update_certificate_manager(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    certificate_manager_update_request_factory: CertificateManagerUpdateRequestFactory,
) -> None:
    api_connector.certificate_managers.update_certificate_manager(
        certificate_manager_update_request_factory.build(), id_=faker.pyint()
    )


def test_read_certificate_manager(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.certificate_managers.read_certificate_manager(id_=faker.pyint())


def test_delete_certificate_manager(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.certificate_managers.delete_certificate_manager(id_=faker.pyint())


def test_request_certificate(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.certificate_managers.request_certificate(id_=faker.pyint())


def test_list_certificate_managers(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.certificate_managers.list_certificate_managers()
