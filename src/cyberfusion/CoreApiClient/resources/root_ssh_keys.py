from cyberfusion.CoreApiClient import models

from cyberfusion.CoreApiClient.interfaces import Resource
from cyberfusion.CoreApiClient._helpers import construct_includes_query_parameter
from cyberfusion.CoreApiClient.http import DtoResponse


class RootSshKeys(Resource):
    def create_public_root_ssh_key(
        self,
        request: models.RootSshKeyCreatePublicRequest,
    ) -> DtoResponse[models.RootSshKeyResource]:
        local_response = self.api_connector.send_or_fail(
            "POST",
            "/api/v1/root-ssh-keys/public",
            data=request.model_dump(exclude_unset=True),
            query_parameters={},
        )

        return DtoResponse.from_responses(local_response, models.RootSshKeyResource)

    def create_private_root_ssh_key(
        self,
        request: models.RootSshKeyCreatePrivateRequest,
    ) -> DtoResponse[models.RootSshKeyResource]:
        local_response = self.api_connector.send_or_fail(
            "POST",
            "/api/v1/root-ssh-keys/private",
            data=request.model_dump(exclude_unset=True),
            query_parameters={},
        )

        return DtoResponse.from_responses(local_response, models.RootSshKeyResource)

    def list_root_ssh_keys(
        self,
        *,
        include_filters: models.RootSshKeysSearchRequest | None = None,
        includes: list[str] | None = None,
    ) -> DtoResponse[list[models.RootSshKeyResource]]:
        local_responses = self.api_connector.send_or_fail_with_auto_pagination(
            "GET",
            "/api/v1/root-ssh-keys",
            data=None,
            query_parameters=(
                include_filters.model_dump(exclude_unset=True)
                if include_filters
                else {}
            )
            | construct_includes_query_parameter(includes),
        )

        return DtoResponse.from_responses(local_responses, models.RootSshKeyResource)

    def read_root_ssh_key(
        self,
        *,
        id_: int,
        includes: list[str] | None = None,
    ) -> DtoResponse[models.RootSshKeyResource]:
        local_response = self.api_connector.send_or_fail(
            "GET",
            f"/api/v1/root-ssh-keys/{id_}",
            data=None,
            query_parameters=construct_includes_query_parameter(includes),
        )

        return DtoResponse.from_responses(local_response, models.RootSshKeyResource)

    def delete_root_ssh_key(
        self,
        *,
        id_: int,
    ) -> DtoResponse[models.DetailMessage]:
        local_response = self.api_connector.send_or_fail(
            "DELETE", f"/api/v1/root-ssh-keys/{id_}", data=None, query_parameters={}
        )

        return DtoResponse.from_responses(local_response, models.DetailMessage)
