from cyberfusion.CoreApiClient.connector import CoreApiConnector
from tests.conftest import (
    MailAccountUpdateRequestFactory,
    MailAccountCreateRequestFactory,
)
import faker


def test_create_mail_account(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    mail_account_create_request_factory: MailAccountCreateRequestFactory,
) -> None:
    api_connector.mail_accounts.create_mail_account(
        mail_account_create_request_factory.build()
    )


def test_update_mail_account(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    mail_account_update_request_factory: MailAccountUpdateRequestFactory,
) -> None:
    api_connector.mail_accounts.update_mail_account(
        mail_account_update_request_factory.build(), id_=faker.pyint()
    )


def test_read_mail_account(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.mail_accounts.read_mail_account(id_=faker.pyint())


def test_delete_mail_account(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.mail_accounts.delete_mail_account(id_=faker.pyint())


def test_list_mail_accounts(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.mail_accounts.list_mail_accounts()


def test_list_mail_account_usages(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.mail_accounts.list_mail_account_usages(
        id_=faker.pyint(), timestamp=faker.date_time()
    )
