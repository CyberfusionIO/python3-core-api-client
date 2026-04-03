from cyberfusion.CoreApiClient import models
from cyberfusion.CoreApiClient._helpers import construct_includes_query_parameter
from cyberfusion.CoreApiClient.http import DtoResponse
from cyberfusion.CoreApiClient.interfaces import Resource


class UrlRedirects(Resource):
    def create_url_redirect(
        self,
        request: models.UrlRedirectCreateRequest,
    ) -> DtoResponse[models.UrlRedirectResource]:
        local_response = self.api_connector.send_or_fail(
            "POST",
            "/api/v1/url-redirects",
            data=request.model_dump(exclude_unset=True),
            query_parameters={},
        )

        return DtoResponse.from_responses(local_response, models.UrlRedirectResource)

    def list_url_redirects(
        self,
        *,
        include_filters: models.UrlRedirectsSearchRequest | None = None,
        includes: list[str] | None = None,
    ) -> DtoResponse[list[models.UrlRedirectResource]]:
        local_responses = self.api_connector.send_or_fail_with_auto_pagination(
            "GET",
            "/api/v1/url-redirects",
            data=None,
            query_parameters=(
                include_filters.model_dump(exclude_unset=True)
                if include_filters
                else {}
            )
            | construct_includes_query_parameter(includes),
        )

        return DtoResponse.from_responses(local_responses, models.UrlRedirectResource)

    def read_url_redirect(
        self,
        *,
        id_: int,
        includes: list[str] | None = None,
    ) -> DtoResponse[models.UrlRedirectResource]:
        local_response = self.api_connector.send_or_fail(
            "GET",
            f"/api/v1/url-redirects/{id_}",
            data=None,
            query_parameters=construct_includes_query_parameter(includes),
        )

        return DtoResponse.from_responses(local_response, models.UrlRedirectResource)

    def update_url_redirect(
        self,
        request: models.UrlRedirectUpdateRequest,
        *,
        id_: int,
    ) -> DtoResponse[models.UrlRedirectResource]:
        local_response = self.api_connector.send_or_fail(
            "PATCH",
            f"/api/v1/url-redirects/{id_}",
            data=request.model_dump(exclude_unset=True),
            query_parameters={},
        )

        return DtoResponse.from_responses(local_response, models.UrlRedirectResource)

    def delete_url_redirect(
        self,
        *,
        id_: int,
    ) -> DtoResponse[models.DetailMessage]:
        local_response = self.api_connector.send_or_fail(
            "DELETE", f"/api/v1/url-redirects/{id_}", data=None, query_parameters={}
        )

        return DtoResponse.from_responses(local_response, models.DetailMessage)
