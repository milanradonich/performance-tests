import time
from typing import TypedDict

from httpx import Response

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client
from clients.http.gateway.users.schema import (
    GetUserResponseSchema,
    CreateUserResponseSchema,
    CreateUserRequestSchema
)


class UsersGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/users сервиса http-gateway
    """
    def get_user_api(self, user_id: str) -> Response:
        """
        GET запрос на получение пользователя по его идентификатору
        :param user_id: идентификатор пользователя
        :return: объект httpx.Response с данными пользователя
        """
        return self.get(f"/api/v1/users/{user_id}")

    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """
        POST запрос на создание пользователя
        :param request: словарь с данными пользователя (email, lastName, firstName, middleName, phoneNumber)
        :return: объект httpx.Response с данными созданного пользователя
        """
        return self.post(f"/api/v1/users", json=request.model_dump(by_alias=True))

    def get_user(self, user_id: str) -> GetUserResponseSchema:
        """
        Получает данные пользователя по его идентификатору
        :param user_id: идентификатор пользователя
        :return: словарь с данными пользователя
        """
        response = self.get_user_api(user_id)
        #return GetUserResponseSchema(**response.json()) #1
        return GetUserResponseSchema.model_validate_json(response.text) #2!

    def create_user(self) -> CreateUserResponseSchema:
        """
        Создает пользователя со сгенерированным уникальным email
        :return: словарь с данными созданного пользователя
        """
        request = CreateUserRequestSchema(
            # email=f"user_{time.time()}@example.com",
            # last_name='string',
            # first_name='string',
            # middle_name='string',
            # phone_number='string',
        )
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)


def build_users_gateway_http_client() -> UsersGatewayHTTPClient:
    """
    Функция создает экземпляр UsersGatewayHTTPClient с настроенным HTTPClient
    :return: Готовый к использованию UsersGatewayHTTPClient
    """
    return UsersGatewayHTTPClient(client=build_gateway_http_client())
