from typing import Any

from httpx import Client, QueryParams, URL, Response


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

    def get(self, url: URL | str, params: QueryParams | None = None) -> Response:
        """
        Выполняет GET запрос
        :param url: адрес эндпоинта
        :param params: query-параметры запроса
        :return: объект httpx.Response с ответом сервера
        """
        return self.client.get(url, params=params)

    def post(self, url: URL | str, json: Any | None = None) -> Response:
        """
        Выполняет POST запрос
        :param url: адрес эндпоинта
        :param json: тело запроса в формате JSON
        :return: объект httpx.Response с ответом сервера
        """
        return self.client.post(url, json=json)

