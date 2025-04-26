from cyberfusion.CoreApiClient.connector import CoreApiConnector
from tests.conftest import (
    TemporaryFtpUserCreateRequestFactory,
    FtpUserUpdateRequestFactory,
    FtpUserCreateRequestFactory,
)
import faker


def test_create_ftp_user(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    ftp_user_create_request_factory: FtpUserCreateRequestFactory,
) -> None:
    api_connector.ftp_users.create_ftp_user(ftp_user_create_request_factory.build())


def test_update_ftp_user(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    ftp_user_update_request_factory: FtpUserUpdateRequestFactory,
) -> None:
    api_connector.ftp_users.update_ftp_user(
        ftp_user_update_request_factory.build(), id_=faker.pyint()
    )


def test_create_temporary_ftp_user(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    temporary_ftp_user_create_request_factory: TemporaryFtpUserCreateRequestFactory,
) -> None:
    api_connector.ftp_users.create_temporary_ftp_user(
        temporary_ftp_user_create_request_factory.build(),
    )


def test_read_ftp_user(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.ftp_users.read_ftp_user(id_=faker.pyint())


def test_delete_ftp_user(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.ftp_users.delete_ftp_user(id_=faker.pyint())


def test_list_ftp_users(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.ftp_users.list_ftp_users()
