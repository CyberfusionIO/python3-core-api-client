from cyberfusion.CoreApiClient import models
from cyberfusion.CoreApiClient.interfaces import Resource
from cyberfusion.CoreApiClient._helpers import construct_includes_query_parameter
from cyberfusion.CoreApiClient.http import DtoResponse


class ScheduledActions(Resource):
    def list_scheduled_actions(
        self,
        *,
        include_filters: models.ScheduledActionsSearchRequest | None = None,
        includes: list[str] | None = None,
    ) -> DtoResponse[list[models.ScheduledActionResource]]:
        local_responses = self.api_connector.send_or_fail_with_auto_pagination(
            "GET",
            "/api/v1/scheduled-actions",
            data=None,
            query_parameters=(
                include_filters.model_dump(exclude_unset=True)
                if include_filters
                else {}
            )
            | construct_includes_query_parameter(includes),
        )

        return DtoResponse.from_responses(
            local_responses, models.ScheduledActionResource
        )

    def read_scheduled_action(
        self,
        *,
        id_: int,
        includes: list[str] | None = None,
    ) -> DtoResponse[models.ScheduledActionResource]:
        local_response = self.api_connector.send_or_fail(
            "GET",
            f"/api/v1/scheduled-actions/{id_}",
            data=None,
            query_parameters=construct_includes_query_parameter(includes),
        )

        return DtoResponse.from_responses(
            local_response, models.ScheduledActionResource
        )

    def delete_scheduled_action(
        self,
        *,
        id_: int,
    ) -> DtoResponse[models.DetailMessage]:
        local_response = self.api_connector.send_or_fail(
            "DELETE",
            f"/api/v1/scheduled-actions/{id_}",
            data=None,
            query_parameters={},
        )

        return DtoResponse.from_responses(local_response, models.DetailMessage)

    def update_scheduled_action(
        self,
        request: models.ScheduledActionUpdateRequest,
        *,
        id_: int,
        includes: list[str] | None = None,
    ) -> DtoResponse[models.ScheduledActionResource]:
        local_response = self.api_connector.send_or_fail(
            "PATCH",
            f"/api/v1/scheduled-actions/{id_}",
            data=request.model_dump(exclude_unset=True),
            query_parameters=construct_includes_query_parameter(includes),
        )

        return DtoResponse.from_responses(
            local_response, models.ScheduledActionResource
        )
