from cyberfusion.CoreApiClient import models
from cyberfusion.CoreApiClient.interfaces import Resource
from cyberfusion.CoreApiClient._helpers import construct_includes_query_parameter
from cyberfusion.CoreApiClient.http import DtoResponse


class SecurityTxtPolicies(Resource):
    def create_security_txt_policy(
        self,
        request: models.SecurityTxtPolicyCreateRequest,
    ) -> DtoResponse[models.SecurityTxtPolicyResource]:
        local_response = self.api_connector.send_or_fail(
            "POST",
            "/api/v1/security-txt-policies",
            data=request.model_dump(exclude_unset=True),
            query_parameters={},
        )

        return DtoResponse.from_response(
            local_response, models.SecurityTxtPolicyResource
        )

    def list_security_txt_policies(
        self,
        *,
        page: int = 1,
        per_page: int = 50,
        include_filters: models.SecurityTxtPoliciesSearchRequest | None = None,
        includes: list[str] | None = None,
    ) -> DtoResponse[list[models.SecurityTxtPolicyResource]]:
        local_response = self.api_connector.send_or_fail(
            "GET",
            "/api/v1/security-txt-policies",
            data=None,
            query_parameters={
                "page": page,
                "per_page": per_page,
            }
            | (
                include_filters.model_dump(exclude_unset=True)
                if include_filters
                else {}
            )
            | construct_includes_query_parameter(includes),
        )

        return DtoResponse.from_response(
            local_response, models.SecurityTxtPolicyResource
        )

    def read_security_txt_policy(
        self,
        *,
        id_: int,
        includes: list[str] | None = None,
    ) -> DtoResponse[models.SecurityTxtPolicyResource]:
        local_response = self.api_connector.send_or_fail(
            "GET",
            f"/api/v1/security-txt-policies/{id_}",
            data=None,
            query_parameters=construct_includes_query_parameter(includes),
        )

        return DtoResponse.from_response(
            local_response, models.SecurityTxtPolicyResource
        )

    def update_security_txt_policy(
        self,
        request: models.SecurityTxtPolicyUpdateRequest,
        *,
        id_: int,
    ) -> DtoResponse[models.SecurityTxtPolicyResource]:
        local_response = self.api_connector.send_or_fail(
            "PATCH",
            f"/api/v1/security-txt-policies/{id_}",
            data=request.model_dump(exclude_unset=True),
            query_parameters={},
        )

        return DtoResponse.from_response(
            local_response, models.SecurityTxtPolicyResource
        )

    def delete_security_txt_policy(
        self,
        *,
        id_: int,
    ) -> DtoResponse[models.DetailMessage]:
        local_response = self.api_connector.send_or_fail(
            "DELETE",
            f"/api/v1/security-txt-policies/{id_}",
            data=None,
            query_parameters={},
        )

        return DtoResponse.from_response(local_response, models.DetailMessage)
