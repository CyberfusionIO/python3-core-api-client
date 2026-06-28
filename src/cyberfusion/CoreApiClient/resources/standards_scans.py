from cyberfusion.CoreApiClient import models

from cyberfusion.CoreApiClient._helpers import construct_includes_query_parameter
from cyberfusion.CoreApiClient.http import DtoResponse
from cyberfusion.CoreApiClient.interfaces import Resource


class StandardsScans(Resource):
    def list_standards_scans(
        self,
        *,
        include_filters: models.StandardsScansSearchRequest | None = None,
        includes: list[str] | None = None,
    ) -> DtoResponse[list[models.StandardsScanResource]]:
        local_responses = self.api_connector.send_or_fail_with_auto_pagination(
            "GET",
            "/api/v1/standards-scans",
            data=None,
            query_parameters=(
                include_filters.model_dump(exclude_unset=True)
                if include_filters
                else {}
            )
            | construct_includes_query_parameter(includes),
        )

        return DtoResponse.from_responses(local_responses, models.StandardsScanResource)

    def read_standards_scan(
        self,
        *,
        id_: int,
        includes: list[str] | None = None,
    ) -> DtoResponse[models.StandardsScanResource]:
        local_response = self.api_connector.send_or_fail(
            "GET",
            f"/api/v1/standards-scans/{id_}",
            data=None,
            query_parameters=construct_includes_query_parameter(includes),
        )

        return DtoResponse.from_responses(local_response, models.StandardsScanResource)

    def read_standards_scan_results(
        self,
        *,
        id_: int,
    ) -> DtoResponse[models.StandardsScanResults]:
        local_response = self.api_connector.send_or_fail(
            "GET",
            f"/api/v1/standards-scans/{id_}/results",
            data=None,
            query_parameters={},
        )

        return DtoResponse.from_responses(local_response, models.StandardsScanResults)
