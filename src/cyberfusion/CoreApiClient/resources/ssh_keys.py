from cyberfusion.CoreApiClient import models

from cyberfusion.CoreApiClient.interfaces import Resource
from cyberfusion.CoreApiClient._helpers import construct_includes_query_parameter
from cyberfusion.CoreApiClient.http import DtoResponse


class SshKeys(Resource):
    def create_public_ssh_key(
        self,
        request: models.SshKeyCreatePublicRequest,
    ) -> DtoResponse[models.SshKeyResource]:
        local_response = self.api_connector.send_or_fail(
            "POST",
            "/api/v1/ssh-keys/public",
            data=request.model_dump(exclude_unset=True),
            query_parameters={},
        )

        return DtoResponse.from_responses(local_response, models.SshKeyResource)

    def create_private_ssh_key(
        self,
        request: models.SshKeyCreatePrivateRequest,
    ) -> DtoResponse[models.SshKeyResource]:
        local_response = self.api_connector.send_or_fail(
            "POST",
            "/api/v1/ssh-keys/private",
            data=request.model_dump(exclude_unset=True),
            query_parameters={},
        )

        return DtoResponse.from_responses(local_response, models.SshKeyResource)

    def list_ssh_keys(
        self,
        *,
        include_filters: models.SshKeysSearchRequest | None = None,
        includes: list[str] | None = None,
    ) -> DtoResponse[list[models.SshKeyResource]]:
        local_responses = self.api_connector.send_or_fail_with_auto_pagination(
            "GET",
            "/api/v1/ssh-keys",
            data=None,
            query_parameters=(
                include_filters.model_dump(exclude_unset=True)
                if include_filters
                else {}
            )
            | construct_includes_query_parameter(includes),
        )

        return DtoResponse.from_responses(local_responses, models.SshKeyResource)

    def read_ssh_key(
        self,
        *,
        id_: int,
        includes: list[str] | None = None,
    ) -> DtoResponse[models.SshKeyResource]:
        local_response = self.api_connector.send_or_fail(
            "GET",
            f"/api/v1/ssh-keys/{id_}",
            data=None,
            query_parameters=construct_includes_query_parameter(includes),
        )

        return DtoResponse.from_responses(local_response, models.SshKeyResource)

    def delete_ssh_key(
        self,
        *,
        id_: int,
    ) -> DtoResponse[models.DetailMessage]:
        local_response = self.api_connector.send_or_fail(
            "DELETE", f"/api/v1/ssh-keys/{id_}", data=None, query_parameters={}
        )

        return DtoResponse.from_responses(local_response, models.DetailMessage)
