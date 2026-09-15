from cyberfusion.CoreApiClient import models

from cyberfusion.CoreApiClient.interfaces import Resource
from cyberfusion.CoreApiClient.http import DtoResponse


class TaskCollections(Resource):
    def list_task_collection_results(
        self,
        *,
        uuid: str,
    ) -> DtoResponse[list[models.TaskResult]]:
        local_response = self.api_connector.send_or_fail(
            "GET",
            f"/api/v1/task-collections/{uuid}/results",
            data=None,
            query_parameters={},
        )

        return DtoResponse.from_responses(local_response, models.TaskResult)
