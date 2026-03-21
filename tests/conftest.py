import pytest
from pydantic import BaseModel
from pytest_mock import MockerFixture
from cyberfusion.CoreApiClient.connector import CoreApiConnector
from _pytest.config.argparsing import Parser
import faker
from polyfactory.factories.pydantic_factory import ModelFactory
from polyfactory.pytest_plugin import register_fixture

from cyberfusion.CoreApiClient import models
from typing import TypeVar, Generic

T = TypeVar("T")


class UpdateFactory(Generic[T], ModelFactory[T]):
    __is_base_factory__ = True

    # Don't generate None as a value. For updates, all values are nullable, but
    # that is meant to indicate that the value can be omitted from the partial
    # update, not that the value itself can be set to None when specified.
    #
    # There are cases in which None is a valid value, but we can't distinguish
    # such cases.

    __allow_none_optionals__ = False


@register_fixture
class BodyLoginAccessTokenFactory(ModelFactory[models.BodyLoginAccessToken]): ...


@register_fixture
class CustomerIPAddressCreateRequestFactory(
    ModelFactory[models.CustomerIpAddressCreateRequest]
): ...


@register_fixture
class HaproxyListenCreateRequestFactory(
    ModelFactory[models.HaproxyListenCreateRequest]
): ...


@register_fixture
class HaproxyListenToNodeCreateRequestFactory(
    ModelFactory[models.HaproxyListenToNodeCreateRequest]
): ...


@register_fixture
class BorgRepositoryCreateRequestFactory(
    ModelFactory[models.BorgRepositoryCreateRequest]
): ...


@register_fixture
class BorgRepositoryUpdateRequestFactory(
    UpdateFactory[models.BorgRepositoryUpdateRequest]
): ...


@register_fixture
class BorgArchiveCreateRequestFactory(
    ModelFactory[models.BorgArchiveCreateRequest]
): ...


@register_fixture
class CertificateCreateRequestFactory(
    ModelFactory[models.CertificateCreateRequest]
): ...


@register_fixture
class CertificateManagerCreateRequestFactory(
    ModelFactory[models.CertificateManagerCreateRequest]
): ...


@register_fixture
class CertificateManagerUpdateRequestFactory(
    UpdateFactory[models.CertificateManagerUpdateRequest]
): ...


@register_fixture
class ClusterCreateRequestFactory(ModelFactory[models.ClusterCreateRequest]): ...


@register_fixture
class ClusterUpdateRequestFactory(UpdateFactory[models.ClusterUpdateRequest]): ...


@register_fixture
class ClusterIPAddressCreateRequestFactory(
    ModelFactory[models.ClusterIpAddressCreateRequest]
): ...


@register_fixture
class VirtualHostCreateRequestFactory(
    ModelFactory[models.VirtualHostCreateRequest]
): ...


@register_fixture
class VirtualHostUpdateRequestFactory(
    UpdateFactory[models.VirtualHostUpdateRequest]
): ...


@register_fixture
class MailHostnameCreateRequestFactory(
    ModelFactory[models.MailHostnameCreateRequest]
): ...


@register_fixture
class MailHostnameUpdateRequestFactory(
    UpdateFactory[models.MailHostnameUpdateRequest]
): ...


@register_fixture
class DomainRouterUpdateRequestFactory(
    UpdateFactory[models.DomainRouterUpdateRequest]
): ...


@register_fixture
class UrlRedirectCreateRequestFactory(
    ModelFactory[models.UrlRedirectCreateRequest]
): ...


@register_fixture
class UrlRedirectUpdateRequestFactory(
    UpdateFactory[models.UrlRedirectUpdateRequest]
): ...


@register_fixture
class HtpasswdFileCreateRequestFactory(
    ModelFactory[models.HtpasswdFileCreateRequest]
): ...


@register_fixture
class HtpasswdUserCreateRequestFactory(
    ModelFactory[models.HtpasswdUserCreateRequest]
): ...


@register_fixture
class HtpasswdUserUpdateRequestFactory(
    UpdateFactory[models.HtpasswdUserUpdateRequest]
): ...


@register_fixture
class BasicAuthenticationRealmCreateRequestFactory(
    ModelFactory[models.BasicAuthenticationRealmCreateRequest]
): ...


@register_fixture
class BasicAuthenticationRealmUpdateRequestFactory(
    UpdateFactory[models.BasicAuthenticationRealmUpdateRequest]
): ...


@register_fixture
class NodeAddOnCreateRequestFactory(ModelFactory[models.NodeAddOnCreateRequest]): ...


@register_fixture
class CronCreateRequestFactory(ModelFactory[models.CronCreateRequest]): ...


@register_fixture
class CronUpdateRequestFactory(UpdateFactory[models.CronUpdateRequest]): ...


@register_fixture
class DaemonCreateRequestFactory(ModelFactory[models.DaemonCreateRequest]): ...


@register_fixture
class DaemonUpdateRequestFactory(UpdateFactory[models.DaemonUpdateRequest]): ...


@register_fixture
class MariadbEncryptionKeyCreateRequestFactory(
    ModelFactory[models.MariadbEncryptionKeyCreateRequest]
): ...


@register_fixture
class FirewallRuleCreateRequestFactory(
    ModelFactory[models.FirewallRuleCreateRequest]
): ...


@register_fixture
class HostsEntryCreateRequestFactory(ModelFactory[models.HostsEntryCreateRequest]): ...


@register_fixture
class SecurityTxtPolicyCreateRequestFactory(
    ModelFactory[models.SecurityTxtPolicyCreateRequest]
): ...


@register_fixture
class SecurityTxtPolicyUpdateRequestFactory(
    UpdateFactory[models.SecurityTxtPolicyUpdateRequest]
): ...


@register_fixture
class FirewallGroupCreateRequestFactory(
    ModelFactory[models.FirewallGroupCreateRequest]
): ...


@register_fixture
class FirewallGroupUpdateRequestFactory(
    UpdateFactory[models.FirewallGroupUpdateRequest]
): ...


@register_fixture
class CustomConfigSnippetCreateFromContentsRequestFactory(
    ModelFactory[models.CustomConfigSnippetCreateFromContentsRequest]
): ...


@register_fixture
class CustomConfigSnippetCreateFromTemplateRequestFactory(
    ModelFactory[models.CustomConfigSnippetCreateFromTemplateRequest]
): ...


@register_fixture
class CustomConfigSnippetUpdateRequestFactory(
    UpdateFactory[models.CustomConfigSnippetUpdateRequest]
): ...


@register_fixture
class CustomConfigCreateRequestFactory(
    ModelFactory[models.CustomConfigCreateRequest]
): ...


@register_fixture
class CustomConfigUpdateRequestFactory(
    UpdateFactory[models.CustomConfigUpdateRequest]
): ...


@register_fixture
class FtpUserCreateRequestFactory(ModelFactory[models.FtpUserCreateRequest]): ...


@register_fixture
class FtpUserUpdateRequestFactory(UpdateFactory[models.FtpUserUpdateRequest]): ...


@register_fixture
class TemporaryFtpUserCreateRequestFactory(
    ModelFactory[models.TemporaryFtpUserCreateRequest]
): ...


@register_fixture
class CmsCreateRequestFactory(ModelFactory[models.CmsCreateRequest]): ...


@register_fixture
class CmsInstallWordpressRequestFactory(
    ModelFactory[models.CmsInstallWordpressRequest]
): ...


@register_fixture
class CmsInstallNextcloudRequestFactory(
    ModelFactory[models.CmsInstallNextcloudRequest]
): ...


@register_fixture
class CmsOptionUpdateRequestFactory(ModelFactory[models.CmsOptionUpdateRequest]): ...


@register_fixture
class CmsConfigurationConstantUpdateRequestFactory(
    ModelFactory[models.CmsConfigurationConstantUpdateRequest]
): ...


@register_fixture
class CmsUserCredentialsUpdateRequestFactory(
    ModelFactory[models.CmsUserCredentialsUpdateRequest]
): ...


@register_fixture
class CmsThemeInstallFromRepositoryRequestFactory(
    ModelFactory[models.CmsThemeInstallFromRepositoryRequest]
): ...


@register_fixture
class CmsThemeInstallFromUrlRequestFactory(
    ModelFactory[models.CmsThemeInstallFromUrlRequest]
): ...


@register_fixture
class FpmPoolCreateRequestFactory(ModelFactory[models.FpmPoolCreateRequest]): ...


@register_fixture
class FpmPoolUpdateRequestFactory(UpdateFactory[models.FpmPoolUpdateRequest]): ...


@register_fixture
class PassengerAppCreateNodejsRequestFactory(
    ModelFactory[models.PassengerAppCreateNodejsRequest]
): ...


@register_fixture
class PassengerAppUpdateRequestFactory(
    UpdateFactory[models.PassengerAppUpdateRequest]
): ...


@register_fixture
class RedisInstanceCreateRequestFactory(
    ModelFactory[models.RedisInstanceCreateRequest]
): ...


@register_fixture
class RedisInstanceUpdateRequestFactory(
    UpdateFactory[models.RedisInstanceUpdateRequest]
): ...


@register_fixture
class N8nInstanceCreateRequestFactory(
    ModelFactory[models.N8nInstanceCreateRequest]
): ...


@register_fixture
class N8nInstanceUpdateRequestFactory(
    UpdateFactory[models.N8nInstanceUpdateRequest]
): ...


@register_fixture
class NodeCreateRequestFactory(ModelFactory[models.NodeCreateRequest]): ...


@register_fixture
class NodeUpdateRequestFactory(UpdateFactory[models.NodeUpdateRequest]): ...


@register_fixture
class UnixUserCreateRequestFactory(ModelFactory[models.UnixUserCreateRequest]): ...


@register_fixture
class UnixUserUpdateRequestFactory(UpdateFactory[models.UnixUserUpdateRequest]): ...


@register_fixture
class SshKeyCreatePublicRequestFactory(
    ModelFactory[models.SshKeyCreatePublicRequest]
): ...


@register_fixture
class SshKeyCreatePrivateRequestFactory(
    ModelFactory[models.SshKeyCreatePrivateRequest]
): ...


@register_fixture
class RootSshKeyCreatePublicRequestFactory(
    ModelFactory[models.RootSshKeyCreatePublicRequest]
): ...


@register_fixture
class RootSshKeyCreatePrivateRequestFactory(
    ModelFactory[models.RootSshKeyCreatePrivateRequest]
): ...


@register_fixture
class DatabaseCreateRequestFactory(ModelFactory[models.DatabaseCreateRequest]): ...


@register_fixture
class DatabaseUpdateRequestFactory(UpdateFactory[models.DatabaseUpdateRequest]): ...


@register_fixture
class DatabaseUserCreateRequestFactory(
    ModelFactory[models.DatabaseUserCreateRequest]
): ...


@register_fixture
class DatabaseUserUpdateRequestFactory(
    UpdateFactory[models.DatabaseUserUpdateRequest]
): ...


@register_fixture
class DatabaseUserGrantCreateRequestFactory(
    ModelFactory[models.DatabaseUserGrantCreateRequest]
): ...


@register_fixture
class MailDomainCreateRequestFactory(ModelFactory[models.MailDomainCreateRequest]): ...


@register_fixture
class MailDomainUpdateRequestFactory(UpdateFactory[models.MailDomainUpdateRequest]): ...


@register_fixture
class MailAccountCreateRequestFactory(
    ModelFactory[models.MailAccountCreateRequest]
): ...


@register_fixture
class MailAccountUpdateRequestFactory(
    UpdateFactory[models.MailAccountUpdateRequest]
): ...


@register_fixture
class MailAliasCreateRequestFactory(ModelFactory[models.MailAliasCreateRequest]): ...


@register_fixture
class MailAliasUpdateRequestFactory(UpdateFactory[models.MailAliasUpdateRequest]): ...


@register_fixture
class ClusterBorgPropertiesCreateRequestFactory(
    ModelFactory[models.ClusterBorgPropertiesCreateRequest]
): ...


@register_fixture
class ClusterElasticsearchPropertiesCreateRequestFactory(
    ModelFactory[models.ClusterElasticsearchPropertiesCreateRequest]
): ...


@register_fixture
class ClusterFirewallPropertiesCreateRequestFactory(
    ModelFactory[models.ClusterFirewallPropertiesCreateRequest]
): ...


@register_fixture
class ClusterGrafanaPropertiesCreateRequestFactory(
    ModelFactory[models.ClusterGrafanaPropertiesCreateRequest]
): ...


@register_fixture
class ClusterKernelcarePropertiesCreateRequestFactory(
    ModelFactory[models.ClusterKernelcarePropertiesCreateRequest]
): ...


@register_fixture
class ClusterMariadbPropertiesCreateRequestFactory(
    ModelFactory[models.ClusterMariadbPropertiesCreateRequest]
): ...


@register_fixture
class ClusterMeilisearchPropertiesCreateRequestFactory(
    ModelFactory[models.ClusterMeilisearchPropertiesCreateRequest]
): ...


@register_fixture
class ClusterMetabasePropertiesCreateRequestFactory(
    ModelFactory[models.ClusterMetabasePropertiesCreateRequest]
): ...


@register_fixture
class ClusterNewRelicPropertiesCreateRequestFactory(
    ModelFactory[models.ClusterNewRelicPropertiesCreateRequest]
): ...


@register_fixture
class ClusterNodejsPropertiesCreateRequestFactory(
    ModelFactory[models.ClusterNodejsPropertiesCreateRequest]
): ...


@register_fixture
class ClusterOsPropertiesCreateRequestFactory(
    ModelFactory[models.ClusterOsPropertiesCreateRequest]
): ...


@register_fixture
class ClusterPhpPropertiesCreateRequestFactory(
    ModelFactory[models.ClusterPhpPropertiesCreateRequest]
): ...


@register_fixture
class ClusterPostgresqlPropertiesCreateRequestFactory(
    ModelFactory[models.ClusterPostgresqlPropertiesCreateRequest]
): ...


@register_fixture
class ClusterRabbitmqPropertiesCreateRequestFactory(
    ModelFactory[models.ClusterRabbitmqPropertiesCreateRequest]
): ...


@register_fixture
class ClusterRedisPropertiesCreateRequestFactory(
    ModelFactory[models.ClusterRedisPropertiesCreateRequest]
): ...


@register_fixture
class ClusterSinglestorePropertiesCreateRequestFactory(
    ModelFactory[models.ClusterSinglestorePropertiesCreateRequest]
): ...


@register_fixture
class ClusterBorgPropertiesUpdateRequestFactory(
    UpdateFactory[models.ClusterBorgPropertiesUpdateRequest]
): ...


@register_fixture
class ClusterSinglestorePropertiesUpdateRequestFactory(
    UpdateFactory[models.ClusterSinglestorePropertiesUpdateRequest]
): ...


@register_fixture
class ClusterRedisPropertiesUpdateRequestFactory(
    UpdateFactory[models.ClusterRedisPropertiesUpdateRequest]
): ...


@register_fixture
class ClusterElasticsearchPropertiesUpdateRequestFactory(
    UpdateFactory[models.ClusterElasticsearchPropertiesUpdateRequest]
): ...


@register_fixture
class ClusterFirewallPropertiesUpdateRequestFactory(
    UpdateFactory[models.ClusterFirewallPropertiesUpdateRequest]
): ...


@register_fixture
class ClusterGrafanaPropertiesUpdateRequestFactory(
    UpdateFactory[models.ClusterGrafanaPropertiesUpdateRequest]
): ...


@register_fixture
class ClusterKernelcarePropertiesUpdateRequestFactory(
    UpdateFactory[models.ClusterKernelcarePropertiesUpdateRequest]
): ...


@register_fixture
class ClusterLoadBalancingPropertiesUpdateRequestFactory(
    UpdateFactory[models.ClusterLoadBalancingPropertiesUpdateRequest]
): ...


@register_fixture
class ClusterMariadbPropertiesUpdateRequestFactory(
    UpdateFactory[models.ClusterMariadbPropertiesUpdateRequest]
): ...


@register_fixture
class ClusterMeilisearchPropertiesUpdateRequestFactory(
    UpdateFactory[models.ClusterMeilisearchPropertiesUpdateRequest]
): ...


@register_fixture
class ClusterMetabasePropertiesUpdateRequestFactory(
    UpdateFactory[models.ClusterMetabasePropertiesUpdateRequest]
): ...


@register_fixture
class ClusterNewRelicPropertiesUpdateRequestFactory(
    UpdateFactory[models.ClusterNewRelicPropertiesUpdateRequest]
): ...


@register_fixture
class ClusterNodejsPropertiesUpdateRequestFactory(
    UpdateFactory[models.ClusterNodejsPropertiesUpdateRequest]
): ...


@register_fixture
class ClusterOsPropertiesUpdateRequestFactory(
    UpdateFactory[models.ClusterOsPropertiesUpdateRequest]
): ...


@register_fixture
class ClusterPhpPropertiesUpdateRequestFactory(
    UpdateFactory[models.ClusterPhpPropertiesUpdateRequest]
): ...


@register_fixture
class ClusterPostgresqlPropertiesUpdateRequestFactory(
    UpdateFactory[models.ClusterPostgresqlPropertiesUpdateRequest]
): ...


@register_fixture
class ClusterRabbitmqPropertiesUpdateRequestFactory(
    UpdateFactory[models.ClusterRabbitmqPropertiesUpdateRequest]
): ...


@register_fixture
class FpmPoolUpdateSettingsRequestFactory(
    UpdateFactory[models.FpmPoolUpdateSettingsRequest]
): ...


@pytest.fixture
def api_connector(faker: faker.Faker, base_url: str) -> CoreApiConnector:
    return CoreApiConnector(
        base_url=base_url,
        username=faker.user_name(),
        password=faker.password(),
    )


def pytest_addoption(parser: Parser) -> None:
    parser.addoption("--server-url", action="store", required=True)


@pytest.fixture
def base_url(request: pytest.FixtureRequest) -> str:
    return request.config.getoption("--server-url")


@pytest.fixture(autouse=True)
def mock_model_validate(mocker: MockerFixture) -> None:
    mocker.patch.object(BaseModel, "model_validate", return_value=lambda x: x)
