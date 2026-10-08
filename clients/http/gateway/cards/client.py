from httpx import Response

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client
from clients.http.gateway.cards.schema import (IssueVirtualCardRequestSchema,
                                               IssuePhysicalCardRequestSchema,
                                               IssueVirtualCardResponseSchema, IssuePhysicalCardResponseSchema
                                               )


class CardsGatewayHTTPClient(HTTPClient):
    """Клиент для взаимодействия с /api/v1/cards сервиса http-gateway"""

    def issue_virtual_card_api(self, request: IssueVirtualCardRequestSchema) -> Response:
        """
        Метод для создания виртуальной карты
        :param request: словарь с данными пользователя и счета
        :return: ответ от сервера (httpx.Response)
        """
        return self.post(f"/api/v1/cards/issue-virtual-card", json=request.model_dump(by_alias=True))

    def issue_physical_card_api(self, request: IssuePhysicalCardRequestSchema) -> Response:
        """
        Метод для создания физической карты
        :param request: словарь с данными пользователя и счета
        :return: ответ от сервера (httpx.Response)
        """
        return self.post(f"/api/v1/cards/issue-physical-card", request.model_dump(by_alias=True))

    def issue_virtual_card(self, user_id: str, account_id: str) -> IssueVirtualCardResponseSchema:
        """
        Выпускает виртуальную карту
        :param user_id: идентификатор пользователя
        :param account_id: идентификатор счета
        :return: словарь с данными выпущенной карты
        """
        request = IssueVirtualCardRequestSchema(user_id=user_id, account_id=account_id)
        response = self.issue_virtual_card_api(request)
        return IssueVirtualCardResponseSchema.model_validate_json(response.text)

    def issue_physical_card(self, user_id: str, account_id: str) -> IssuePhysicalCardResponseSchema:
        """
        Выпускает физическую карту
        :param account_id: идентификатор счета
        :param user_id: идентификатор пользователя
        :return: словарь с данными выпущенной карты
        """
        request = IssuePhysicalCardRequestSchema(user_id=user_id, account_id=account_id)
        response = self.issue_physical_card_api(request)
        return IssuePhysicalCardResponseSchema.model_validate_json(response.text)


def build_cards_gateway_http_client() -> CardsGatewayHTTPClient:
    """
    Функция создает экземпляр CardsGatewayHTTPClient с настроенным HTTPClient
    :return: Готовый к использованию CardsGatewayHTTPClient
    """
    return CardsGatewayHTTPClient(client=build_gateway_http_client())