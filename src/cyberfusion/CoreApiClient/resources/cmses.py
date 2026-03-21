from cyberfusion.CoreApiClient import models
from typing import Optional, Union

from cyberfusion.CoreApiClient._helpers import construct_includes_query_parameter
from cyberfusion.CoreApiClient.http import DtoResponse
from cyberfusion.CoreApiClient.interfaces import Resource


class Cmses(Resource):
    def create_cms(
        self,
        request: models.CmsCreateRequest,
    ) -> DtoResponse[models.CmsResource]:
        local_response = self.api_connector.send_or_fail(
            "POST",
            "/api/v1/cmses",
            data=request.model_dump(exclude_unset=True),
            query_parameters={},
        )

        return DtoResponse.from_response(local_response, models.CmsResource)

    def list_cmses(
        self,
        *,
        page: int = 1,
        per_page: int = 50,
        include_filters: models.CmsesSearchRequest | None = None,
        includes: list[str] | None = None,
    ) -> DtoResponse[list[models.CmsResource]]:
        local_response = self.api_connector.send_or_fail(
            "GET",
            "/api/v1/cmses",
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

        return DtoResponse.from_response(local_response, models.CmsResource)

    def read_cms(
        self,
        *,
        id_: int,
        includes: list[str] | None = None,
    ) -> DtoResponse[models.CmsResource]:
        local_response = self.api_connector.send_or_fail(
            "GET",
            f"/api/v1/cmses/{id_}",
            data=None,
            query_parameters=construct_includes_query_parameter(includes),
        )

        return DtoResponse.from_response(local_response, models.CmsResource)

    def delete_cms(
        self,
        *,
        id_: int,
    ) -> DtoResponse[models.DetailMessage]:
        local_response = self.api_connector.send_or_fail(
            "DELETE", f"/api/v1/cmses/{id_}", data=None, query_parameters={}
        )

        return DtoResponse.from_response(local_response, models.DetailMessage)

    def install_wordpress(
        self,
        request: models.CmsInstallWordpressRequest,
        *,
        id_: int,
        callback_url: Optional[str] = None,
    ) -> DtoResponse[models.TaskCollectionResource]:
        local_response = self.api_connector.send_or_fail(
            "POST",
            f"/api/v1/cmses/{id_}/install/wordpress",
            data=request.model_dump(exclude_unset=True),
            query_parameters={
                "callback_url": callback_url,
            },
        )

        return DtoResponse.from_response(local_response, models.TaskCollectionResource)

    def install_nextcloud(
        self,
        request: models.CmsInstallNextcloudRequest,
        *,
        id_: int,
        callback_url: Optional[str] = None,
    ) -> DtoResponse[models.TaskCollectionResource]:
        local_response = self.api_connector.send_or_fail(
            "POST",
            f"/api/v1/cmses/{id_}/install/nextcloud",
            data=request.model_dump(exclude_unset=True),
            query_parameters={
                "callback_url": callback_url,
            },
        )

        return DtoResponse.from_response(local_response, models.TaskCollectionResource)

    def get_cms_one_time_login(
        self,
        *,
        id_: int,
    ) -> DtoResponse[models.CmsOneTimeLogin]:
        local_response = self.api_connector.send_or_fail(
            "GET",
            f"/api/v1/cmses/{id_}/one-time-login",
            data=None,
            query_parameters={},
        )

        return DtoResponse.from_response(local_response, models.CmsOneTimeLogin)

    def get_cms_plugins(
        self,
        *,
        id_: int,
    ) -> DtoResponse[list[models.CmsPlugin]]:
        local_response = self.api_connector.send_or_fail(
            "GET", f"/api/v1/cmses/{id_}/plugins", data=None, query_parameters={}
        )

        return DtoResponse.from_response(local_response, models.CmsPlugin)

    def update_cms_option(
        self,
        request: models.CmsOptionUpdateRequest,
        *,
        id_: int,
        name: models.CmsOptionNameEnum,
    ) -> DtoResponse[models.CmsOption]:
        local_response = self.api_connector.send_or_fail(
            "PATCH",
            f"/api/v1/cmses/{id_}/options/{name}",
            data=request.model_dump(exclude_unset=True),
            query_parameters={},
        )

        return DtoResponse.from_response(local_response, models.CmsOption)

    def update_cms_configuration_constant(
        self,
        request: models.CmsConfigurationConstantUpdateRequest,
        *,
        id_: int,
        name: str,
    ) -> DtoResponse[models.CmsConfigurationConstant]:
        local_response = self.api_connector.send_or_fail(
            "PATCH",
            f"/api/v1/cmses/{id_}/configuration-constants/{name}",
            data=request.model_dump(exclude_unset=True),
            query_parameters={},
        )

        return DtoResponse.from_response(
            local_response, models.CmsConfigurationConstant
        )

    def update_cms_user_credentials(
        self,
        request: models.CmsUserCredentialsUpdateRequest,
        *,
        id_: int,
        user_id: int,
    ) -> DtoResponse[models.DetailMessage]:
        local_response = self.api_connector.send_or_fail(
            "PATCH",
            f"/api/v1/cmses/{id_}/users/{user_id}/credentials",
            data=request.model_dump(exclude_unset=True),
            query_parameters={},
        )

        return DtoResponse.from_response(local_response, models.DetailMessage)

    def update_cms_core(
        self,
        *,
        id_: int,
        callback_url: Optional[str] = None,
    ) -> DtoResponse[models.TaskCollectionResource]:
        local_response = self.api_connector.send_or_fail(
            "POST",
            f"/api/v1/cmses/{id_}/core/update",
            data=None,
            query_parameters={
                "callback_url": callback_url,
            },
        )

        return DtoResponse.from_response(local_response, models.TaskCollectionResource)

    def update_cms_plugin(
        self,
        *,
        id_: int,
        name: str,
        callback_url: Optional[str] = None,
    ) -> DtoResponse[models.TaskCollectionResource]:
        local_response = self.api_connector.send_or_fail(
            "POST",
            f"/api/v1/cmses/{id_}/plugins/{name}/update",
            data=None,
            query_parameters={
                "callback_url": callback_url,
            },
        )

        return DtoResponse.from_response(local_response, models.TaskCollectionResource)

    def search_replace_in_cms_database(
        self,
        *,
        id_: int,
        search_string: str,
        replace_string: str,
        callback_url: Optional[str] = None,
    ) -> DtoResponse[models.TaskCollectionResource]:
        local_response = self.api_connector.send_or_fail(
            "POST",
            f"/api/v1/cmses/{id_}/search-replace",
            data=None,
            query_parameters={
                "callback_url": callback_url,
                "search_string": search_string,
                "replace_string": replace_string,
            },
        )

        return DtoResponse.from_response(local_response, models.TaskCollectionResource)

    def enable_cms_plugin(
        self,
        *,
        id_: int,
        name: str,
    ) -> DtoResponse[models.DetailMessage]:
        local_response = self.api_connector.send_or_fail(
            "POST",
            f"/api/v1/cmses/{id_}/plugins/{name}/enable",
            data=None,
            query_parameters={},
        )

        return DtoResponse.from_response(local_response, models.DetailMessage)

    def disable_cms_plugin(
        self,
        *,
        id_: int,
        name: str,
    ) -> DtoResponse[models.DetailMessage]:
        local_response = self.api_connector.send_or_fail(
            "POST",
            f"/api/v1/cmses/{id_}/plugins/{name}/disable",
            data=None,
            query_parameters={},
        )

        return DtoResponse.from_response(local_response, models.DetailMessage)

    def regenerate_cms_salts(
        self,
        *,
        id_: int,
    ) -> DtoResponse[models.DetailMessage]:
        local_response = self.api_connector.send_or_fail(
            "POST",
            f"/api/v1/cmses/{id_}/regenerate-salts",
            data=None,
            query_parameters={},
        )

        return DtoResponse.from_response(local_response, models.DetailMessage)

    def install_cms_theme(
        self,
        request: Union[
            models.CmsThemeInstallFromRepositoryRequest,
            models.CmsThemeInstallFromUrlRequest,
        ],
        *,
        id_: int,
    ) -> DtoResponse[models.DetailMessage]:
        local_response = self.api_connector.send_or_fail(
            "POST",
            f"/api/v1/cmses/{id_}/themes",
            data=request.model_dump(exclude_unset=True),
            query_parameters={},
        )

        return DtoResponse.from_response(local_response, models.DetailMessage)
