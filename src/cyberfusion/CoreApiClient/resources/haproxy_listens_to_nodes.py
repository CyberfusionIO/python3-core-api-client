from cyberfusion.CoreApiClient import models

from cyberfusion.CoreApiClient.interfaces import Resource
from cyberfusion.CoreApiClient._helpers import construct_includes_query_parameter
from cyberfusion.CoreApiClient.http import DtoResponse


class HaproxyListensToNodes(Resource):
    def create_haproxy_listen_to_node(
        self,
        request: models.HaproxyListenToNodeCreateRequest,
    ) -> DtoResponse[models.HaproxyListenToNodeResource]:
        local_response = self.api_connector.send_or_fail(
            "POST",
            "/api/v1/haproxy-listens-to-nodes",
            data=request.model_dump(exclude_unset=True),
            query_parameters={},
        )

        return DtoResponse.from_responses(
            local_response, models.HaproxyListenToNodeResource
        )

    def list_haproxy_listens_to_nodes(
        self,
        *,
        include_filters: models.HaproxyListensToNodesSearchRequest | None = None,
        includes: list[str] | None = None,
    ) -> DtoResponse[list[models.HaproxyListenToNodeResource]]:
        local_responses = self.api_connector.send_or_fail_with_auto_pagination(
            "GET",
            "/api/v1/haproxy-listens-to-nodes",
            data=None,
            query_parameters=(
                include_filters.model_dump(exclude_unset=True)
                if include_filters
                else {}
            )
            | construct_includes_query_parameter(includes),
        )

        return DtoResponse.from_responses(
            local_responses, models.HaproxyListenToNodeResource
        )

    def read_haproxy_listen_to_node(
        self,
        *,
        id_: int,
        includes: list[str] | None = None,
    ) -> DtoResponse[models.HaproxyListenToNodeResource]:
        local_response = self.api_connector.send_or_fail(
            "GET",
            f"/api/v1/haproxy-listens-to-nodes/{id_}",
            data=None,
            query_parameters=construct_includes_query_parameter(includes),
        )

        return DtoResponse.from_responses(
            local_response, models.HaproxyListenToNodeResource
        )

    def delete_haproxy_listen_to_node(
        self,
        *,
        id_: int,
    ) -> DtoResponse[models.DetailMessage]:
        local_response = self.api_connector.send_or_fail(
            "DELETE",
            f"/api/v1/haproxy-listens-to-nodes/{id_}",
            data=None,
            query_parameters={},
        )

        return DtoResponse.from_responses(local_response, models.DetailMessage)
