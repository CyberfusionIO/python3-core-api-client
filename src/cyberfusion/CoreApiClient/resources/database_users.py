from cyberfusion.CoreApiClient import models
from datetime import datetime
from cyberfusion.CoreApiClient._helpers import construct_includes_query_parameter
from cyberfusion.CoreApiClient.http import DtoResponse
from cyberfusion.CoreApiClient.interfaces import Resource


class DatabaseUsers(Resource):
    def create_database_user(
        self,
        request: models.DatabaseUserCreateRequest,
    ) -> DtoResponse[models.DatabaseUserResource]:
        local_response = self.api_connector.send_or_fail(
            "POST",
            "/api/v1/database-users",
            data=request.model_dump(exclude_unset=True),
            query_parameters={},
        )

        return DtoResponse.from_responses(local_response, models.DatabaseUserResource)

    def list_database_users(
        self,
        *,
        include_filters: models.DatabaseUsersSearchRequest | None = None,
        includes: list[str] | None = None,
    ) -> DtoResponse[list[models.DatabaseUserResource]]:
        local_responses = self.api_connector.send_or_fail_with_auto_pagination(
            "GET",
            "/api/v1/database-users",
            data=None,
            query_parameters=(
                include_filters.model_dump(exclude_unset=True)
                if include_filters
                else {}
            )
            | construct_includes_query_parameter(includes),
        )

        return DtoResponse.from_responses(local_responses, models.DatabaseUserResource)

    def read_database_user(
        self,
        *,
        id_: int,
        includes: list[str] | None = None,
    ) -> DtoResponse[models.DatabaseUserResource]:
        local_response = self.api_connector.send_or_fail(
            "GET",
            f"/api/v1/database-users/{id_}",
            data=None,
            query_parameters=construct_includes_query_parameter(includes),
        )

        return DtoResponse.from_responses(local_response, models.DatabaseUserResource)

    def update_database_user(
        self,
        request: models.DatabaseUserUpdateRequest,
        *,
        id_: int,
    ) -> DtoResponse[models.DatabaseUserResource]:
        local_response = self.api_connector.send_or_fail(
            "PATCH",
            f"/api/v1/database-users/{id_}",
            data=request.model_dump(exclude_unset=True),
            query_parameters={},
        )

        return DtoResponse.from_responses(local_response, models.DatabaseUserResource)

    def delete_database_user(
        self,
        *,
        id_: int,
    ) -> DtoResponse[models.DetailMessage]:
        local_response = self.api_connector.send_or_fail(
            "DELETE",
            f"/api/v1/database-users/{id_}",
            data=None,
            query_parameters={},
        )

        return DtoResponse.from_responses(local_response, models.DetailMessage)

    def read_database_user_metrics(
        self,
        *,
        id_: int,
        start_timestamp: datetime,
        end_timestamp: datetime,
    ) -> DtoResponse[models.DatabaseUsersMetricsResource]:
        local_response = self.api_connector.send_or_fail(
            "GET",
            f"/api/v1/database-users/{id_}/metrics",
            data=None,
            query_parameters={
                "start_timestamp": start_timestamp,
                "end_timestamp": end_timestamp,
            },
        )

        return DtoResponse.from_responses(
            local_response, models.DatabaseUsersMetricsResource
        )
