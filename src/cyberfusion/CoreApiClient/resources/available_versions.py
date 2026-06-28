from cyberfusion.CoreApiClient import models

from cyberfusion.CoreApiClient._helpers import construct_includes_query_parameter
from cyberfusion.CoreApiClient.http import DtoResponse
from cyberfusion.CoreApiClient.interfaces import Resource


class AvailableVersions(Resource):
    def list_available_nodejs_versions(
        self,
        *,
        includes: list[str] | None = None,
    ) -> DtoResponse[list[models.NodejsVersionResource]]:
        local_responses = self.api_connector.send_or_fail_with_auto_pagination(
            "GET",
            "/api/v1/available-versions/nodejs",
            data=None,
            query_parameters=construct_includes_query_parameter(includes),
        )

        return DtoResponse.from_responses(local_responses, models.NodejsVersionResource)

    def list_available_php_versions(
        self,
        *,
        includes: list[str] | None = None,
    ) -> DtoResponse[list[models.PhpVersionResource]]:
        local_responses = self.api_connector.send_or_fail_with_auto_pagination(
            "GET",
            "/api/v1/available-versions/php",
            data=None,
            query_parameters=construct_includes_query_parameter(includes),
        )

        return DtoResponse.from_responses(local_responses, models.PhpVersionResource)

    def list_available_wordpress_versions(
        self,
        *,
        includes: list[str] | None = None,
    ) -> DtoResponse[list[models.WordpressVersionResource]]:
        local_responses = self.api_connector.send_or_fail_with_auto_pagination(
            "GET",
            "/api/v1/available-versions/wordpress",
            data=None,
            query_parameters=construct_includes_query_parameter(includes),
        )

        return DtoResponse.from_responses(
            local_responses, models.WordpressVersionResource
        )
