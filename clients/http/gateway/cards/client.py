from typing import TypedDict

from httpx import Response

from clients.http.client import HTTPClient


class IssueCardRequestDict(TypedDict):
    userId: str
    accountId: str


class CardsGatewayHTTPClient(HTTPClient):
    """Клиент для взаимодействия с /api/v1/cards сервиса http-gateway"""

    def issue_virtual_card_api(self, request: IssueCardRequestDict) -> Response:
        """
        Метод для создания виртуальной карты
        :param request: словарь с данными пользователя и счета
        :return: ответ от сервера (httpx.Response)
        """
        return self.post(f"/api/v1/cards/issue-virtual-card", json=request)

    def issue_physical_card_api(self, request: IssueCardRequestDict) -> Response:
        """
        Метод для создания физической карты
        :param request: словарь с данными пользователя и счета
        :return: ответ от сервера (httpx.Response)
        """
        return self.post(f"/api/v1/cards/issue-physical-card", json=request)

