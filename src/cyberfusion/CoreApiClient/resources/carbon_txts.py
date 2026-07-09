from cyberfusion.CoreApiClient import models
from cyberfusion.CoreApiClient.interfaces import Resource
from cyberfusion.CoreApiClient._helpers import construct_includes_query_parameter
from cyberfusion.CoreApiClient.http import DtoResponse


class CarbonTxts(Resource):
    def create_carbon_txt_policy(
        self,
        request: models.CarbonTxtCreateRequest,
    ) -> DtoResponse[models.CarbonTxtResource]:
        local_response = self.api_connector.send_or_fail(
            "POST",
            "/api/v1/carbon-txts",
            data=request.model_dump(exclude_unset=True),
            query_parameters={},
        )

        return DtoResponse.from_responses(local_response, models.CarbonTxtResource)

    def list_carbon_txt_policies(
        self,
        *,
        include_filters: models.CarbonTxtsSearchRequest | None = None,
        includes: list[str] | None = None,
    ) -> DtoResponse[list[models.CarbonTxtResource]]:
        local_responses = self.api_connector.send_or_fail_with_auto_pagination(
            "GET",
            "/api/v1/carbon-txts",
            data=None,
            query_parameters=(
                include_filters.model_dump(exclude_unset=True)
                if include_filters
                else {}
            )
            | construct_includes_query_parameter(includes),
        )

        return DtoResponse.from_responses(local_responses, models.CarbonTxtResource)

    def read_carbon_txt_policy(
        self,
        *,
        id_: int,
        includes: list[str] | None = None,
    ) -> DtoResponse[models.CarbonTxtResource]:
        local_response = self.api_connector.send_or_fail(
            "GET",
            f"/api/v1/carbon-txts/{id_}",
            data=None,
            query_parameters=construct_includes_query_parameter(includes),
        )

        return DtoResponse.from_responses(local_response, models.CarbonTxtResource)

    def update_carbon_txt_policy(
        self,
        request: models.CarbonTxtUpdateRequest,
        *,
        id_: int,
    ) -> DtoResponse[models.CarbonTxtResource]:
        local_response = self.api_connector.send_or_fail(
            "PATCH",
            f"/api/v1/carbon-txts/{id_}",
            data=request.model_dump(exclude_unset=True),
            query_parameters={},
        )

        return DtoResponse.from_responses(local_response, models.CarbonTxtResource)

    def delete_carbon_txt_policy(
        self,
        *,
        id_: int,
    ) -> DtoResponse[models.DetailMessage]:
        local_response = self.api_connector.send_or_fail(
            "DELETE",
            f"/api/v1/carbon-txts/{id_}",
            data=None,
            query_parameters={},
        )

        return DtoResponse.from_responses(local_response, models.DetailMessage)
