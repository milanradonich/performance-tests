import time
from typing import TypedDict

from httpx import Response

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class UserDict(TypedDict):
    """
    Структура данных пользователя
    """
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str
    phoneNumber: str


class GetUserResponseDict(TypedDict):
    """
    Структура ответа на получение пользователя
    """
    user: UserDict


class CreateUserRequestDict(TypedDict):
    """
    Структура запроса на создание пользователя
    """
    email: str
    lastName: str
    firstName: str
    middleName: str
    phoneNumber: str

class CreateUserResponseDict(TypedDict):
    """
    Структура ответа на создание пользователя
    """
    user: UserDict



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

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        POST запрос на создание пользователя
        :param request: словарь с данными пользователя (email, lastName, firstName, middleName, phoneNumber)
        :return: объект httpx.Response с данными созданного пользователя
        """
        return self.post(f"/api/v1/users", json=request)

    def get_user(self, user_id: str) -> GetUserResponseDict:
        """
        Получает данные пользователя по его идентификатору
        :param user_id: идентификатор пользователя
        :return: словарь с данными пользователя
        """
        response = self.get_user_api(user_id)
        return response.json()

    def create_user(self) -> CreateUserResponseDict:
        """
        Создает пользователя со сгенерированным уникальным email
        :return: словарь с данными созданного пользователя
        """
        request = CreateUserRequestDict(
            email=f"user_{time.time()}@example.com",
            lastName='string',
            firstName='string',
            middleName='string',
            phoneNumber='string',
        )
        response = self.create_user_api(request)
        return response.json()


def build_users_gateway_http_client() -> UsersGatewayHTTPClient:
    """
    Функция создает экземпляр UsersGatewayHTTPClient с настроенным HTTPClient
    :return: Готовый к использованию UsersGatewayHTTPClient
    """
    return UsersGatewayHTTPClient(client=build_gateway_http_client())
