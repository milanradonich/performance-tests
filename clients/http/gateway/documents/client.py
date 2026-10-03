from typing import TypedDict

from httpx import Response

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class DocumentDict(TypedDict):
    """
    Структура ответа получения документов
    """
    url: str
    document: str


class GetTariffDocumentResponseDict(TypedDict):
    """Структура ответа на получение документа по тарифу"""
    tariff: DocumentDict


class GetContractDocumentResponseDict(TypedDict):
    """Структура ответа на получение документа по контракту"""
    contract: DocumentDict


class DocumentsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/documents
    """
    def get_tariff_document_api(self, account_id: str) -> Response:
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

    def get_tariff_document(self, account_id: str) -> GetTariffDocumentResponseDict:
        """
        Получение документа по тарифу
        :param account_id:
        :return: ответ запроса и ссылка на документ
        """
        response = self.get_tariff_document_api(account_id)
        return response.json()

    def get_contract_document(self, account_id: str) -> GetContractDocumentResponseDict:
        """
        Получение документа по контракту
        :param account_id:
        :return: ответ запроса и ссылка на документ
        """
        response = self.get_contract_document_api(account_id)
        return response.json()


def build_documents_gateway_http_client() -> DocumentsGatewayHTTPClient:
    """
    Функция создает экземпляр DocumentsGatewayHTTPClient с настроенным HTTPClient
    :return: Готовый к использованию DocumentsGatewayHTTPClient
    """
    return DocumentsGatewayHTTPClient(client=build_gateway_http_client())
