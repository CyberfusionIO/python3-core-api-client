from cyberfusion.CoreApiClient import models

from cyberfusion.CoreApiClient.interfaces import Resource
from cyberfusion.CoreApiClient._helpers import construct_includes_query_parameter
from cyberfusion.CoreApiClient.http import DtoResponse


class HtpasswdUsers(Resource):
    def create_htpasswd_user(
        self,
        request: models.HtpasswdUserCreateRequest,
    ) -> DtoResponse[models.HtpasswdUserResource]:
        local_response = self.api_connector.send_or_fail(
            "POST",
            "/api/v1/htpasswd-users",
            data=request.model_dump(exclude_unset=True),
            query_parameters={},
        )

        return DtoResponse.from_responses(local_response, models.HtpasswdUserResource)

    def list_htpasswd_users(
        self,
        *,
        include_filters: models.HtpasswdUsersSearchRequest | None = None,
        includes: list[str] | None = None,
    ) -> DtoResponse[list[models.HtpasswdUserResource]]:
        local_responses = self.api_connector.send_or_fail_with_auto_pagination(
            "GET",
            "/api/v1/htpasswd-users",
            data=None,
            query_parameters=(
                include_filters.model_dump(exclude_unset=True)
                if include_filters
                else {}
            )
            | construct_includes_query_parameter(includes),
        )

        return DtoResponse.from_responses(local_responses, models.HtpasswdUserResource)

    def read_htpasswd_user(
        self,
        *,
        id_: int,
        includes: list[str] | None = None,
    ) -> DtoResponse[models.HtpasswdUserResource]:
        local_response = self.api_connector.send_or_fail(
            "GET",
            f"/api/v1/htpasswd-users/{id_}",
            data=None,
            query_parameters=construct_includes_query_parameter(includes),
        )

        return DtoResponse.from_responses(local_response, models.HtpasswdUserResource)

    def update_htpasswd_user(
        self,
        request: models.HtpasswdUserUpdateRequest,
        *,
        id_: int,
    ) -> DtoResponse[models.HtpasswdUserResource]:
        local_response = self.api_connector.send_or_fail(
            "PATCH",
            f"/api/v1/htpasswd-users/{id_}",
            data=request.model_dump(exclude_unset=True),
            query_parameters={},
        )

        return DtoResponse.from_responses(local_response, models.HtpasswdUserResource)

    def delete_htpasswd_user(
        self,
        *,
        id_: int,
    ) -> DtoResponse[models.DetailMessage]:
        local_response = self.api_connector.send_or_fail(
            "DELETE",
            f"/api/v1/htpasswd-users/{id_}",
            data=None,
            query_parameters={},
        )

        return DtoResponse.from_responses(local_response, models.DetailMessage)
