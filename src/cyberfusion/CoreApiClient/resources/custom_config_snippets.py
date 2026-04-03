from cyberfusion.CoreApiClient import models
from typing import Union

from cyberfusion.CoreApiClient._helpers import construct_includes_query_parameter
from cyberfusion.CoreApiClient.http import DtoResponse
from cyberfusion.CoreApiClient.interfaces import Resource


class CustomConfigSnippets(Resource):
    def create_custom_config_snippet(
        self,
        request: Union[
            models.CustomConfigSnippetCreateFromContentsRequest,
            models.CustomConfigSnippetCreateFromTemplateRequest,
        ],
    ) -> DtoResponse[models.CustomConfigSnippetResource]:
        local_response = self.api_connector.send_or_fail(
            "POST",
            "/api/v1/custom-config-snippets",
            data=request.model_dump(exclude_unset=True),
            query_parameters={},
        )

        return DtoResponse.from_responses(
            local_response, models.CustomConfigSnippetResource
        )

    def list_custom_config_snippets(
        self,
        *,
        include_filters: models.CustomConfigSnippetsSearchRequest | None = None,
        includes: list[str] | None = None,
    ) -> DtoResponse[list[models.CustomConfigSnippetResource]]:
        local_responses = self.api_connector.send_or_fail_with_auto_pagination(
            "GET",
            "/api/v1/custom-config-snippets",
            data=None,
            query_parameters=(
                include_filters.model_dump(exclude_unset=True)
                if include_filters
                else {}
            )
            | construct_includes_query_parameter(includes),
        )

        return DtoResponse.from_responses(
            local_responses, models.CustomConfigSnippetResource
        )

    def read_custom_config_snippet(
        self,
        *,
        id_: int,
        includes: list[str] | None = None,
    ) -> DtoResponse[models.CustomConfigSnippetResource]:
        local_response = self.api_connector.send_or_fail(
            "GET",
            f"/api/v1/custom-config-snippets/{id_}",
            data=None,
            query_parameters=construct_includes_query_parameter(includes),
        )

        return DtoResponse.from_responses(
            local_response, models.CustomConfigSnippetResource
        )

    def update_custom_config_snippet(
        self,
        request: models.CustomConfigSnippetUpdateRequest,
        *,
        id_: int,
    ) -> DtoResponse[models.CustomConfigSnippetResource]:
        local_response = self.api_connector.send_or_fail(
            "PATCH",
            f"/api/v1/custom-config-snippets/{id_}",
            data=request.model_dump(exclude_unset=True),
            query_parameters={},
        )

        return DtoResponse.from_responses(
            local_response, models.CustomConfigSnippetResource
        )

    def delete_custom_config_snippet(
        self,
        *,
        id_: int,
    ) -> DtoResponse[models.DetailMessage]:
        local_response = self.api_connector.send_or_fail(
            "DELETE",
            f"/api/v1/custom-config-snippets/{id_}",
            data=None,
            query_parameters={},
        )

        return DtoResponse.from_responses(local_response, models.DetailMessage)
