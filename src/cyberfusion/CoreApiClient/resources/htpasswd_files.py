from cyberfusion.CoreApiClient import models

from cyberfusion.CoreApiClient.interfaces import Resource
from cyberfusion.CoreApiClient._helpers import construct_includes_query_parameter
from cyberfusion.CoreApiClient.http import DtoResponse


class HtpasswdFiles(Resource):
    def create_htpasswd_file(
        self,
        request: models.HtpasswdFileCreateRequest,
    ) -> DtoResponse[models.HtpasswdFileResource]:
        local_response = self.api_connector.send_or_fail(
            "POST",
            "/api/v1/htpasswd-files",
            data=request.model_dump(exclude_unset=True),
            query_parameters={},
        )

        return DtoResponse.from_responses(local_response, models.HtpasswdFileResource)

    def list_htpasswd_files(
        self,
        *,
        include_filters: models.HtpasswdFilesSearchRequest | None = None,
        includes: list[str] | None = None,
    ) -> DtoResponse[list[models.HtpasswdFileResource]]:
        local_responses = self.api_connector.send_or_fail_with_auto_pagination(
            "GET",
            "/api/v1/htpasswd-files",
            data=None,
            query_parameters=(
                include_filters.model_dump(exclude_unset=True)
                if include_filters
                else {}
            )
            | construct_includes_query_parameter(includes),
        )

        return DtoResponse.from_responses(local_responses, models.HtpasswdFileResource)

    def read_htpasswd_file(
        self,
        *,
        id_: int,
        includes: list[str] | None = None,
    ) -> DtoResponse[models.HtpasswdFileResource]:
        local_response = self.api_connector.send_or_fail(
            "GET",
            f"/api/v1/htpasswd-files/{id_}",
            data=None,
            query_parameters=construct_includes_query_parameter(includes),
        )

        return DtoResponse.from_responses(local_response, models.HtpasswdFileResource)

    def delete_htpasswd_file(
        self,
        *,
        id_: int,
    ) -> DtoResponse[models.DetailMessage]:
        local_response = self.api_connector.send_or_fail(
            "DELETE",
            f"/api/v1/htpasswd-files/{id_}",
            data=None,
            query_parameters={},
        )

        return DtoResponse.from_responses(local_response, models.DetailMessage)
