from cyberfusion.CoreApiClient.connector import CoreApiConnector
from tests.conftest import (
    MailHostnameUpdateRequestFactory,
    MailHostnameCreateRequestFactory,
)
import faker


def test_create_mail_hostname(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    mail_hostname_create_request_factory: MailHostnameCreateRequestFactory,
) -> None:
    api_connector.mail_hostnames.create_mail_hostname(
        mail_hostname_create_request_factory.build()
    )


def test_update_mail_hostname(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    mail_hostname_update_request_factory: MailHostnameUpdateRequestFactory,
) -> None:
    api_connector.mail_hostnames.update_mail_hostname(
        mail_hostname_update_request_factory.build(), id_=faker.pyint()
    )


def test_read_mail_hostname(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.mail_hostnames.read_mail_hostname(id_=faker.pyint())


def test_delete_mail_hostname(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.mail_hostnames.delete_mail_hostname(id_=faker.pyint())


def test_list_mail_hostnames(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.mail_hostnames.list_mail_hostnames()
