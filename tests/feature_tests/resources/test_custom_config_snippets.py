from cyberfusion.CoreApiClient.connector import CoreApiConnector
from tests.conftest import (
    CustomConfigSnippetUpdateRequestFactory,
    CustomConfigSnippetCreateFromTemplateRequestFactory,
    CustomConfigSnippetCreateFromContentsRequestFactory,
)
import faker


def test_create_custom_config_snippet_from_contents(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    custom_config_snippet_create_from_contents_request_factory: CustomConfigSnippetCreateFromContentsRequestFactory,
) -> None:
    api_connector.custom_config_snippets.create_custom_config_snippet(
        custom_config_snippet_create_from_contents_request_factory.build()
    )


def test_create_custom_config_snippet_from_template(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    custom_config_snippet_create_from_template_request_factory: CustomConfigSnippetCreateFromTemplateRequestFactory,
) -> None:
    api_connector.custom_config_snippets.create_custom_config_snippet(
        custom_config_snippet_create_from_template_request_factory.build()
    )


def test_update_custom_config_snippet(
    api_connector: CoreApiConnector,
    faker: faker.Faker,
    custom_config_snippet_update_request_factory: CustomConfigSnippetUpdateRequestFactory,
) -> None:
    api_connector.custom_config_snippets.update_custom_config_snippet(
        custom_config_snippet_update_request_factory.build(), id_=faker.pyint()
    )


def test_read_custom_config_snippet(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.custom_config_snippets.read_custom_config_snippet(id_=faker.pyint())


def test_delete_custom_config_snippet(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.custom_config_snippets.delete_custom_config_snippet(id_=faker.pyint())


def test_list_custom_config_snippets(
    api_connector: CoreApiConnector, faker: faker.Faker
) -> None:
    api_connector.custom_config_snippets.list_custom_config_snippets()
