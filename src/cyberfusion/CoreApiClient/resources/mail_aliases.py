from cyberfusion.CoreApiClient import models

from cyberfusion.CoreApiClient.interfaces import Resource
from cyberfusion.CoreApiClient._helpers import construct_includes_query_parameter
from cyberfusion.CoreApiClient.http import DtoResponse


class MailAliases(Resource):
    def create_mail_alias(
        self,
        request: models.MailAliasCreateRequest,
    ) -> DtoResponse[models.MailAliasResource]:
        local_response = self.api_connector.send_or_fail(
            "POST",
            "/api/v1/mail-aliases",
            data=request.model_dump(exclude_unset=True),
            query_parameters={},
        )

        return DtoResponse.from_responses(local_response, models.MailAliasResource)

    def list_mail_aliases(
        self,
        *,
        include_filters: models.MailAliasesSearchRequest | None = None,
        includes: list[str] | None = None,
    ) -> DtoResponse[list[models.MailAliasResource]]:
        local_responses = self.api_connector.send_or_fail_with_auto_pagination(
            "GET",
            "/api/v1/mail-aliases",
            data=None,
            query_parameters=(
                include_filters.model_dump(exclude_unset=True)
                if include_filters
                else {}
            )
            | construct_includes_query_parameter(includes),
        )

        return DtoResponse.from_responses(local_responses, models.MailAliasResource)

    def read_mail_alias(
        self,
        *,
        id_: int,
        includes: list[str] | None = None,
    ) -> DtoResponse[models.MailAliasResource]:
        local_response = self.api_connector.send_or_fail(
            "GET",
            f"/api/v1/mail-aliases/{id_}",
            data=None,
            query_parameters=construct_includes_query_parameter(includes),
        )

        return DtoResponse.from_responses(local_response, models.MailAliasResource)

    def update_mail_alias(
        self,
        request: models.MailAliasUpdateRequest,
        *,
        id_: int,
    ) -> DtoResponse[models.MailAliasResource]:
        local_response = self.api_connector.send_or_fail(
            "PATCH",
            f"/api/v1/mail-aliases/{id_}",
            data=request.model_dump(exclude_unset=True),
            query_parameters={},
        )

        return DtoResponse.from_responses(local_response, models.MailAliasResource)

    def delete_mail_alias(
        self,
        *,
        id_: int,
    ) -> DtoResponse[models.DetailMessage]:
        local_response = self.api_connector.send_or_fail(
            "DELETE", f"/api/v1/mail-aliases/{id_}", data=None, query_parameters={}
        )

        return DtoResponse.from_responses(local_response, models.DetailMessage)
