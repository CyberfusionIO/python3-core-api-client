from cyberfusion.CoreApiClient import models
from typing import Optional

from cyberfusion.CoreApiClient.interfaces import Resource
from cyberfusion.CoreApiClient._helpers import construct_includes_query_parameter
from cyberfusion.CoreApiClient.http import DtoResponse


class UnixUsers(Resource):
    def create_unix_user(
        self,
        request: models.UnixUserCreateRequest,
    ) -> DtoResponse[models.UnixUserResource]:
        local_response = self.api_connector.send_or_fail(
            "POST",
            "/api/v1/unix-users",
            data=request.model_dump(exclude_unset=True),
            query_parameters={},
        )

        return DtoResponse.from_response(local_response, models.UnixUserResource)

    def list_unix_users(
        self,
        *,
        page: int = 1,
        per_page: int = 50,
        include_filters: models.UnixUsersSearchRequest | None = None,
        includes: list[str] | None = None,
    ) -> DtoResponse[list[models.UnixUserResource]]:
        local_response = self.api_connector.send_or_fail(
            "GET",
            "/api/v1/unix-users",
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

        return DtoResponse.from_response(local_response, models.UnixUserResource)

    def read_unix_user(
        self,
        *,
        id_: int,
        includes: list[str] | None = None,
    ) -> DtoResponse[models.UnixUserResource]:
        local_response = self.api_connector.send_or_fail(
            "GET",
            f"/api/v1/unix-users/{id_}",
            data=None,
            query_parameters=construct_includes_query_parameter(includes),
        )

        return DtoResponse.from_response(local_response, models.UnixUserResource)

    def update_unix_user(
        self,
        request: models.UnixUserUpdateRequest,
        *,
        id_: int,
    ) -> DtoResponse[models.UnixUserResource]:
        local_response = self.api_connector.send_or_fail(
            "PATCH",
            f"/api/v1/unix-users/{id_}",
            data=request.model_dump(exclude_unset=True),
            query_parameters={},
        )

        return DtoResponse.from_response(local_response, models.UnixUserResource)

    def delete_unix_user(
        self,
        *,
        id_: int,
        delete_on_cluster: Optional[bool] = None,
    ) -> DtoResponse[models.DetailMessage]:
        local_response = self.api_connector.send_or_fail(
            "DELETE",
            f"/api/v1/unix-users/{id_}",
            data=None,
            query_parameters={
                "delete_on_cluster": delete_on_cluster,
            },
        )

        return DtoResponse.from_response(local_response, models.DetailMessage)

    def compare_unix_users(
        self,
        *,
        left_unix_user_id: int,
        right_unix_user_id: int,
    ) -> DtoResponse[models.UnixUserComparison]:
        local_response = self.api_connector.send_or_fail(
            "GET",
            f"/api/v1/unix-users/{left_unix_user_id}/comparison",
            data=None,
            query_parameters={
                "right_unix_user_id": right_unix_user_id,
            },
        )

        return DtoResponse.from_response(local_response, models.UnixUserComparison)

    def list_unix_user_usages(
        self,
        *,
        id_: int,
        timestamp: str,
        time_unit: Optional[models.UnixUserUsageResource] = None,
        includes: list[str] | None = None,
    ) -> DtoResponse[list[models.UnixUserUsageResource]]:
        local_response = self.api_connector.send_or_fail(
            "GET",
            f"/api/v1/unix-users/{id_}/usages",
            data=None,
            query_parameters={
                "timestamp": timestamp,
                "time_unit": time_unit,
            }
            | construct_includes_query_parameter(includes),
        )

        return DtoResponse.from_response(local_response, models.UnixUserUsageResource)
