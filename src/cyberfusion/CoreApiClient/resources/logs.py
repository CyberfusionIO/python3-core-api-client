from cyberfusion.CoreApiClient import models

from cyberfusion.CoreApiClient._helpers import construct_includes_query_parameter
from cyberfusion.CoreApiClient.http import DtoResponse
from cyberfusion.CoreApiClient.interfaces import Resource


class Logs(Resource):
    def list_object_logs(
        self,
        *,
        include_filters: models.ObjectLogsSearchRequest | None = None,
        includes: list[str] | None = None,
    ) -> DtoResponse[list[models.ObjectLogResource]]:
        local_responses = self.api_connector.send_or_fail_with_auto_pagination(
            "GET",
            "/api/v1/object-logs",
            data=None,
            query_parameters=(
                include_filters.model_dump(exclude_unset=True)
                if include_filters
                else {}
            )
            | construct_includes_query_parameter(includes),
        )

        return DtoResponse.from_responses(local_responses, models.ObjectLogResource)

    def list_request_logs(
        self,
        *,
        include_filters: models.RequestLogsSearchRequest | None = None,
        includes: list[str] | None = None,
    ) -> DtoResponse[list[models.RequestLogResource]]:
        local_responses = self.api_connector.send_or_fail_with_auto_pagination(
            "GET",
            "/api/v1/request-logs",
            data=None,
            query_parameters=(
                include_filters.model_dump(exclude_unset=True)
                if include_filters
                else {}
            )
            | construct_includes_query_parameter(includes),
        )

        return DtoResponse.from_responses(local_responses, models.RequestLogResource)
