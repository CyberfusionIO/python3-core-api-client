from cyberfusion.CoreApiClient.connector import CoreApiConnector
from tests.conftest import MailAliasUpdateRequestFactory, MailAliasCreateRequestFactory
import faker


def test_create_mail_alias(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    mail_alias_create_request_factory: MailAliasCreateRequestFactory,
) -> None:
    api_connector.mail_aliases.create_mail_alias(
        mail_alias_create_request_factory.build()
    )


def test_update_mail_alias(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    mail_alias_update_request_factory: MailAliasUpdateRequestFactory,
) -> None:
    api_connector.mail_aliases.update_mail_alias(
        mail_alias_update_request_factory.build(), id_=faker.pyint()
    )


def test_read_mail_alias(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.mail_aliases.read_mail_alias(id_=faker.pyint())


def test_delete_mail_alias(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.mail_aliases.delete_mail_alias(id_=faker.pyint())


def test_list_mail_aliases(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.mail_aliases.list_mail_aliases()
