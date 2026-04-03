from cyberfusion.CoreApiClient import models

from cyberfusion.CoreApiClient.interfaces import Resource
from cyberfusion.CoreApiClient._helpers import construct_includes_query_parameter
from cyberfusion.CoreApiClient.http import DtoResponse


class MariadbEncryptionKeys(Resource):
    def create_mariadb_encryption_key(
        self,
        request: models.MariadbEncryptionKeyCreateRequest,
    ) -> DtoResponse[models.MariadbEncryptionKeyResource]:
        local_response = self.api_connector.send_or_fail(
            "POST",
            "/api/v1/mariadb-encryption-keys",
            data=request.model_dump(exclude_unset=True),
            query_parameters={},
        )

        return DtoResponse.from_responses(
            local_response, models.MariadbEncryptionKeyResource
        )

    def list_mariadb_encryption_keys(
        self,
        *,
        include_filters: models.MariadbEncryptionKeysSearchRequest | None = None,
        includes: list[str] | None = None,
    ) -> DtoResponse[list[models.MariadbEncryptionKeyResource]]:
        local_responses = self.api_connector.send_or_fail_with_auto_pagination(
            "GET",
            "/api/v1/mariadb-encryption-keys",
            data=None,
            query_parameters=(
                include_filters.model_dump(exclude_unset=True)
                if include_filters
                else {}
            )
            | construct_includes_query_parameter(includes),
        )

        return DtoResponse.from_responses(
            local_responses, models.MariadbEncryptionKeyResource
        )

    def read_mariadb_encryption_key(
        self,
        *,
        id_: int,
        includes: list[str] | None = None,
    ) -> DtoResponse[models.MariadbEncryptionKeyResource]:
        local_response = self.api_connector.send_or_fail(
            "GET",
            f"/api/v1/mariadb-encryption-keys/{id_}",
            data=None,
            query_parameters=construct_includes_query_parameter(includes),
        )

        return DtoResponse.from_responses(
            local_response, models.MariadbEncryptionKeyResource
        )
