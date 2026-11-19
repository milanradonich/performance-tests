from typing import Any, TypedDict

from httpx import Client, QueryParams, URL, Response


# Тип расширений, которые можно передать в запрос
# В нашем случае мы используем только параметр "route", но можно добавить и другие
class HTTPClientExtensions(TypedDict, total=False):
    route: str


class HTTPClient:
    """
    Базовый HTTP клиент, обертка над httpx.Client для выполнения GET и POST запросов
    """
    def __init__(self, client: Client):
        """
        Инициализирует HTTP клиент
        :param client: экземпляр httpx.Client для выполнения запросов
        """
        self.client = client

    def get(self,
            url: URL | str,
            params: QueryParams | None = None,
            extensions: HTTPClientExtensions | None = None
            ) -> Response:
        """
        Выполняет GET запрос
        :param extensions: Дополнительные данные, передаваемые через HTTPX extensions.
        :param url: адрес эндпоинта
        :param params: query-параметры запроса
        :return: объект httpx.Response с ответом сервера
        """
        return self.client.get(url, params=params, extensions=extensions)

    def post(self,
             url: URL | str,
             json: Any | None = None,
             extensions: HTTPClientExtensions | None = None) -> Response:
        """
        Выполняет POST запрос
        :param extensions: Дополнительные данные, передаваемые через HTTPX extensions.
        :param url: адрес эндпоинта
        :param json: тело запроса в формате JSON
        :return: объект httpx.Response с ответом сервера
        """
        return self.client.post(url, json=json, extensions=extensions)

