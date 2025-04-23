from cyberfusion.CoreApiClient.connector import CoreApiConnector
import random
from cyberfusion.CoreApiClient import models
from tests.conftest import (
    CmsThemeInstallFromURLRequestFactory,
    CmsThemeInstallFromRepositoryRequestFactory,
    CmsUserCredentialsUpdateRequestFactory,
    CmsConfigurationConstantUpdateRequestFactory,
    CmsOptionUpdateRequestFactory,
    CmsInstallNextCloudRequestFactory,
    CmsInstallWordPressRequestFactory,
    CmsCreateRequestFactory,
)
import faker


def test_create_cms(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    cms_create_request_factory: CmsCreateRequestFactory,
) -> None:
    api_connector.cmses.create_cms(cms_create_request_factory.build())


def test_install_wordpress(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    cms_install_word_press_request_factory: CmsInstallWordPressRequestFactory,
) -> None:
    api_connector.cmses.install_wordpress(
        cms_install_word_press_request_factory.build(), id_=faker.pyint()
    )


def test_install_nextcloud(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    cms_install_next_cloud_request_factory: CmsInstallNextCloudRequestFactory,
) -> None:
    api_connector.cmses.install_nextcloud(
        cms_install_next_cloud_request_factory.build(), id_=faker.pyint()
    )


def test_update_cms_option(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    cms_option_update_request_factory: CmsOptionUpdateRequestFactory,
) -> None:
    api_connector.cmses.update_cms_option(
        cms_option_update_request_factory.build(),
        id_=faker.pyint(),
        name=random.choice(list(models.CMSOptionNameEnum)),
    )


def test_update_cms_configuration_constant(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    cms_configuration_constant_update_request_factory: CmsConfigurationConstantUpdateRequestFactory,
) -> None:
    api_connector.cmses.update_cms_configuration_constant(
        cms_configuration_constant_update_request_factory.build(),
        id_=faker.pyint(),
        name=faker.word(),
    )


def test_update_cms_user_credentials(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    cms_user_credentials_update_request_factory: CmsUserCredentialsUpdateRequestFactory,
) -> None:
    api_connector.cmses.update_cms_user_credentials(
        cms_user_credentials_update_request_factory.build(),
        id_=faker.pyint(),
        user_id=faker.pyint(),
    )


def test_install_cms_theme_from_repository(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    cms_theme_install_from_repository_request_factory: CmsThemeInstallFromRepositoryRequestFactory,
) -> None:
    api_connector.cmses.install_cms_theme(
        cms_theme_install_from_repository_request_factory.build(), id_=faker.pyint()
    )


def test_install_cms_theme_from_url(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    cms_theme_install_from_url_request_factory: CmsThemeInstallFromURLRequestFactory,
) -> None:
    api_connector.cmses.install_cms_theme(
        cms_theme_install_from_url_request_factory.build(), id_=faker.pyint()
    )


def test_read_cms(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.cmses.read_cms(id_=faker.pyint())


def test_delete_cms(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.cmses.delete_cms(id_=faker.pyint())


def test_get_cms_one_time_login(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.cmses.get_cms_one_time_login(id_=faker.pyint())


def test_get_cms_plugins(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.cmses.get_cms_plugins(id_=faker.pyint())


def test_update_cms_core(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.cmses.update_cms_core(id_=faker.pyint())


def test_update_cms_plugin(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.cmses.update_cms_plugin(id_=faker.pyint(), name=faker.word())


def test_search_replace_in_cms_database(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.cmses.search_replace_in_cms_database(
        id_=faker.pyint(), search_string=faker.word(), replace_string=faker.word()
    )


def test_enable_cms_plugin(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.cmses.enable_cms_plugin(id_=faker.pyint(), name=faker.word())


def test_disable_cms_plugin(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.cmses.disable_cms_plugin(id_=faker.pyint(), name=faker.word())


def test_regenerate_cms_salts(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.cmses.regenerate_cms_salts(id_=faker.pyint())


def test_list_cmses(api_connector: CoreApiConnector, faker: faker.Faker) -> None:
    api_connector.cmses.list_cmses()
