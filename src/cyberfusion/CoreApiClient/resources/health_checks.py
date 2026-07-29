from cyberfusion.CoreApiClient import models
from cyberfusion.CoreApiClient.interfaces import Resource
from cyberfusion.CoreApiClient.http import DtoResponse


class HealthChecks(Resource):
    def read_health_check(
        self,
        *,
        id_: int,
    ) -> DtoResponse[models.HealthCheckResource]:
        local_response = self.api_connector.send_or_fail(
            "GET",
            f"/api/v1/health-checks/{id_}",
            data=None,
            query_parameters={},
        )

        return DtoResponse.from_responses(local_response, models.HealthCheckResource)
