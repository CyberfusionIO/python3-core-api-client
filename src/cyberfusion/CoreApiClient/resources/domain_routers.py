from cyberfusion.CoreApiClient import models
from cyberfusion.CoreApiClient.interfaces import Resource
from cyberfusion.CoreApiClient._helpers import construct_includes_query_parameter
from cyberfusion.CoreApiClient.http import DtoResponse


class DomainRouters(Resource):
    def list_domain_routers(
        self,
        *,
        include_filters: models.DomainRoutersSearchRequest | None = None,
        includes: list[str] | None = None,
    ) -> DtoResponse[list[models.DomainRouterResource]]:
        local_responses = self.api_connector.send_or_fail_with_auto_pagination(
            "GET",
            "/api/v1/domain-routers",
            data=None,
            query_parameters=(
                include_filters.model_dump(exclude_unset=True)
                if include_filters
                else {}
            )
            | construct_includes_query_parameter(includes),
        )

        return DtoResponse.from_responses(local_responses, models.DomainRouterResource)

    def update_domain_router(
        self,
        request: models.DomainRouterUpdateRequest,
        *,
        id_: int,
    ) -> DtoResponse[models.DomainRouterResource]:
        local_response = self.api_connector.send_or_fail(
            "PATCH",
            f"/api/v1/domain-routers/{id_}",
            data=request.model_dump(exclude_unset=True),
            query_parameters={},
        )

        return DtoResponse.from_responses(local_response, models.DomainRouterResource)
