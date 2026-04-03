from cyberfusion.CoreApiClient import models

from cyberfusion.CoreApiClient._helpers import construct_includes_query_parameter
from cyberfusion.CoreApiClient.http import DtoResponse
from cyberfusion.CoreApiClient.interfaces import Resource


class CertificateManagers(Resource):
    def create_certificate_manager(
        self,
        request: models.CertificateManagerCreateRequest,
    ) -> DtoResponse[models.CertificateManagerResource]:
        local_response = self.api_connector.send_or_fail(
            "POST",
            "/api/v1/certificate-managers",
            data=request.model_dump(exclude_unset=True),
            query_parameters={},
        )

        return DtoResponse.from_responses(
            local_response, models.CertificateManagerResource
        )

    def list_certificate_managers(
        self,
        *,
        include_filters: models.CertificateManagersSearchRequest | None = None,
        includes: list[str] | None = None,
    ) -> DtoResponse[list[models.CertificateManagerResource]]:
        local_responses = self.api_connector.send_or_fail_with_auto_pagination(
            "GET",
            "/api/v1/certificate-managers",
            data=None,
            query_parameters=(
                include_filters.model_dump(exclude_unset=True)
                if include_filters
                else {}
            )
            | construct_includes_query_parameter(includes),
        )

        return DtoResponse.from_responses(
            local_responses, models.CertificateManagerResource
        )

    def read_certificate_manager(
        self,
        *,
        id_: int,
        includes: list[str] | None = None,
    ) -> DtoResponse[models.CertificateManagerResource]:
        local_response = self.api_connector.send_or_fail(
            "GET",
            f"/api/v1/certificate-managers/{id_}",
            data=None,
            query_parameters=construct_includes_query_parameter(includes),
        )

        return DtoResponse.from_responses(
            local_response, models.CertificateManagerResource
        )

    def update_certificate_manager(
        self,
        request: models.CertificateManagerUpdateRequest,
        *,
        id_: int,
    ) -> DtoResponse[models.CertificateManagerResource]:
        local_response = self.api_connector.send_or_fail(
            "PATCH",
            f"/api/v1/certificate-managers/{id_}",
            data=request.model_dump(exclude_unset=True),
            query_parameters={},
        )

        return DtoResponse.from_responses(
            local_response, models.CertificateManagerResource
        )

    def delete_certificate_manager(
        self,
        *,
        id_: int,
    ) -> DtoResponse[models.DetailMessage]:
        local_response = self.api_connector.send_or_fail(
            "DELETE",
            f"/api/v1/certificate-managers/{id_}",
            data=None,
            query_parameters={},
        )

        return DtoResponse.from_responses(local_response, models.DetailMessage)

    def request_certificate(
        self,
        *,
        id_: int,
    ) -> DtoResponse[models.TaskCollectionResource]:
        local_response = self.api_connector.send_or_fail(
            "POST",
            f"/api/v1/certificate-managers/{id_}/request",
            data=None,
            query_parameters={},
        )

        return DtoResponse.from_responses(local_response, models.TaskCollectionResource)
