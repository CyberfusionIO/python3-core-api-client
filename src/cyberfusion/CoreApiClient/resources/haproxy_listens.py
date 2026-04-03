from cyberfusion.CoreApiClient import models

from cyberfusion.CoreApiClient.interfaces import Resource
from cyberfusion.CoreApiClient._helpers import construct_includes_query_parameter
from cyberfusion.CoreApiClient.http import DtoResponse


class HaproxyListens(Resource):
    def create_haproxy_listen(
        self,
        request: models.HaproxyListenCreateRequest,
    ) -> DtoResponse[models.HaproxyListenResource]:
        local_response = self.api_connector.send_or_fail(
            "POST",
            "/api/v1/haproxy-listens",
            data=request.model_dump(exclude_unset=True),
            query_parameters={},
        )

        return DtoResponse.from_responses(local_response, models.HaproxyListenResource)

    def list_haproxy_listens(
        self,
        *,
        include_filters: models.HaproxyListensSearchRequest | None = None,
        includes: list[str] | None = None,
    ) -> DtoResponse[list[models.HaproxyListenResource]]:
        local_responses = self.api_connector.send_or_fail_with_auto_pagination(
            "GET",
            "/api/v1/haproxy-listens",
            data=None,
            query_parameters=(
                include_filters.model_dump(exclude_unset=True)
                if include_filters
                else {}
            )
            | construct_includes_query_parameter(includes),
        )

        return DtoResponse.from_responses(local_responses, models.HaproxyListenResource)

    def read_haproxy_listen(
        self,
        *,
        id_: int,
        includes: list[str] | None = None,
    ) -> DtoResponse[models.HaproxyListenResource]:
        local_response = self.api_connector.send_or_fail(
            "GET",
            f"/api/v1/haproxy-listens/{id_}",
            data=None,
            query_parameters=construct_includes_query_parameter(includes),
        )

        return DtoResponse.from_responses(local_response, models.HaproxyListenResource)

    def delete_haproxy_listen(
        self,
        *,
        id_: int,
    ) -> DtoResponse[models.DetailMessage]:
        local_response = self.api_connector.send_or_fail(
            "DELETE",
            f"/api/v1/haproxy-listens/{id_}",
            data=None,
            query_parameters={},
        )

        return DtoResponse.from_responses(local_response, models.DetailMessage)
