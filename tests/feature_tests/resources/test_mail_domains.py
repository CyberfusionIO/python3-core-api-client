from cyberfusion.CoreApiClient.connector import CoreApiConnector
from tests.conftest import (
    MailDomainUpdateRequestFactory,
    MailDomainCreateRequestFactory,
)
import faker


def test_create_mail_domain(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    mail_domain_create_request_factory: MailDomainCreateRequestFactory,
) -> None:
    api_connector.mail_domains.create_mail_domain(
        mail_domain_create_request_factory.build()
    )


def test_update_mail_domain(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    mail_domain_update_request_factory: MailDomainUpdateRequestFactory,
) -> None:
    api_connector.mail_domains.update_mail_domain(
        mail_domain_update_request_factory.build(), id_=faker.pyint()
    )


def test_read_mail_domain(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.mail_domains.read_mail_domain(id_=faker.pyint())


def test_delete_mail_domain(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.mail_domains.delete_mail_domain(id_=faker.pyint())


def test_list_mail_domains(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.mail_domains.list_mail_domains()
