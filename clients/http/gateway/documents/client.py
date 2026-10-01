from httpx import Response

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class DocumentsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/documents
    """
    def get_tarif_document_api(self, account_id: str) -> Response:
        """
        Получение тарифа по счету
        :param account_id: id счета
        :return: ответ запроса
        """
        return self.get(f'/api/v1/documents/tariff-document/{account_id}')

    def get_contract_document_api(self, account_id: str) -> Response:
        """
        Получение контракта по счету
        :param account_id: id счета
        :return: ответ запроса
        """
        return self.get(f'/api/v1/documents/contract-document/{account_id}')


def build_documents_gateway_http_client() -> DocumentsGatewayHTTPClient:
    """
    Функция создает экземпляр DocumentsGatewayHTTPClient с настроенным HTTPClient
    :return: Готовый к использованию DocumentsGatewayHTTPClient
    """
    return DocumentsGatewayHTTPClient(client=build_gateway_http_client())