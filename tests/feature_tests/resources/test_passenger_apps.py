# from cyberfusion.CoreApiClient.connector import CoreApiConnector
# from tests.conftest import (
#     PassengerAppUpdateRequestFactory,
#     PassengerAppCreateNodejsRequestFactory,
# )
# import faker
#
#
# def test_create_nodejs_passenger_app(
#     api_connector: CoreApiConnector,
#     faker: faker.Faker,
#     passenger_app_create_nodejs_request_factory: PassengerAppCreateNodejsRequestFactory,
# ) -> None:
#     api_connector.passenger_apps.create_nodejs_passenger_app(
#         passenger_app_create_nodejs_request_factory.build()
#     )
#
#
# def test_update_passenger_app(
#     api_connector: CoreApiConnector,
#     faker: faker.Faker,
#     passenger_app_update_request_factory: PassengerAppUpdateRequestFactory,
# ) -> None:
#     api_connector.passenger_apps.update_passenger_app(
#         passenger_app_update_request_factory.build(), id_=faker.pyint()
#     )
#
#
# def test_read_passenger_app(
#     api_connector: CoreApiConnector, faker: faker.Faker
# ) -> None:
#     api_connector.passenger_apps.read_passenger_app(id_=faker.pyint())
#
#
# def test_delete_passenger_app(
#     api_connector: CoreApiConnector, faker: faker.Faker
# ) -> None:
#     api_connector.passenger_apps.delete_passenger_app(id_=faker.pyint())
#
#
# def test_restart_passenger_app(
#     api_connector: CoreApiConnector, faker: faker.Faker
# ) -> None:
#     api_connector.passenger_apps.restart_passenger_app(id_=faker.pyint())
#
#
# def test_list_passenger_apps(
#     api_connector: CoreApiConnector, faker: faker.Faker
# ) -> None:
#     api_connector.passenger_apps.list_passenger_apps()
