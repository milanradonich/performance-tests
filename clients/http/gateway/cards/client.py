from typing import TypedDict

from httpx import Response

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class CardDict(TypedDict):
    """
    Структура данных карты
    """
    id: str
    pin: str
    cvv: str
    type: str
    status: str
    accountId: str
    cardNumber: str
    cardHolder: str
    expiryDate: str
    paymentSystem: str


class IssueVirtualCardRequestDict(TypedDict):
    """
    Структура запроса на выпуск виртуальной карты
    """
    userId: str
    accountId: str


class IssuePhysicalCardRequestDict(TypedDict):
    """
    Структура запроса на выпуск физической карты
    """
    userId: str
    accountId: str


class IssuePhysicalCardResponseDict(TypedDict):
    """
    Структура ответа на выпуск физической карты
    """
    card: CardDict


class IssueVirtualCardResponseDict(TypedDict):
    """
    Структура ответа на выпуск виртуальной карты
    """
    card: CardDict


class CardsGatewayHTTPClient(HTTPClient):
    """Клиент для взаимодействия с /api/v1/cards сервиса http-gateway"""

    def issue_virtual_card_api(self, request: IssueVirtualCardRequestDict) -> Response:
        """
        Метод для создания виртуальной карты
        :param request: словарь с данными пользователя и счета
        :return: ответ от сервера (httpx.Response)
        """
        return self.post(f"/api/v1/cards/issue-virtual-card", json=request)

    def issue_physical_card_api(self, request: IssuePhysicalCardRequestDict) -> Response:
        """
        Метод для создания физической карты
        :param request: словарь с данными пользователя и счета
        :return: ответ от сервера (httpx.Response)
        """
        return self.post(f"/api/v1/cards/issue-physical-card", json=request)

    def issue_virtual_card(self, userId: str, accountId: str) -> IssueVirtualCardResponseDict:
        """
        Выпускает виртуальную карту
        :param userId: идентификатор пользователя
        :param accountId: идентификатор счета
        :return: словарь с данными выпущенной карты
        """
        request = IssueVirtualCardRequestDict(userId=userId, accountId=accountId)
        response = self.issue_virtual_card_api(request)
        return response.json()

    def issue_physical_card(self, user_id: str, accountId: str) -> IssuePhysicalCardResponseDict:
        """
        Выпускает физическую карту
        :param user_id: идентификатор пользователя
        :param accountId: идентификатор счета
        :return: словарь с данными выпущенной карты
        """
        request = IssuePhysicalCardRequestDict(userId=user_id, accountId=accountId)
        response = self.issue_physical_card_api(request)
        return response.json()


def build_cards_gateway_http_client() -> CardsGatewayHTTPClient:
    """
    Функция создает экземпляр CardsGatewayHTTPClient с настроенным HTTPClient
    :return: Готовый к использованию CardsGatewayHTTPClient
    """
    return CardsGatewayHTTPClient(client=build_gateway_http_client())