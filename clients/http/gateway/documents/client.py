from httpx import Response

from clients.http.client import HTTPClient


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


