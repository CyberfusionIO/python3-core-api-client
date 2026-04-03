import json
from dataclasses import dataclass
from http import HTTPStatus
from typing import Any, TypeVar, Generic

from requests.structures import CaseInsensitiveDict

from cyberfusion.CoreApiClient.models import CoreApiModel

from requests.models import Response as RequestsResponse


ModelType = TypeVar("ModelType", bound=CoreApiModel)

DtoType = TypeVar("DtoType", CoreApiModel, list[CoreApiModel])


@dataclass
class Response:
    status_code: int
    body: str
    headers: CaseInsensitiveDict
    requests_response: RequestsResponse

    @property
    def failed(self) -> bool:
        return self.status_code >= HTTPStatus.BAD_REQUEST

    @property
    def json(self) -> Any:
        return json.loads(self.body)


@dataclass
class DtoResponse(Generic[DtoType]):
    requests_responses: list[RequestsResponse]
    dto: DtoType

    @classmethod
    def from_responses(
        cls, responses: Response | list[Response], model: type[ModelType]
    ) -> "DtoResponse":
        if isinstance(responses, Response):
            responses = [responses]

        dto: list = []

        for response in responses:
            items = response.json

            if isinstance(items, list):
                dto.extend(model.model_validate(object_) for object_ in items)
            else:
                dto.append(model.model_validate(items))

        return cls(
            requests_responses=[r.requests_response for r in responses],
            dto=dto,
        )
