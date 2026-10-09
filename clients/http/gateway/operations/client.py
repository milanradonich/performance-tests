from httpx import Response, QueryParams

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client
from clients.http.gateway.operations.schema import (
    GetOperationsQuerySchema,
    GetOperationsResponseSchema,
    GetOperationsSummaryQuerySchema,
    GetOperationsSummaryResponseSchema,
    GetOperationReceiptResponseSchema,
    GetOperationResponseSchema,
    MakeFeeOperationRequestSchema,
    MakeFeeOperationResponseSchema,
    BaseOperationStatus,
    MakeTopUpOperationRequestSchema,
    MakeTopUpOperationResponseSchema,
    MakeCashbackOperationRequestSchema,
    MakeCashbackOperationResponseSchema,
    MakeTransferOperationRequestSchema,
    MakeTransferOperationResponseSchema,
    MakePurchaseOperationRequestSchema,
    MakePurchaseOperationResponseSchema,
    MakeBillPaymentOperationRequestSchema,
    MakeBillPaymentOperationResponseSchema,
    MakeCashWithdrawalOperationRequestSchema,
    MakeCashWithdrawalOperationResponseSchema
)


class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations
    """

    def get_operations_api(self, query: GetOperationsQuerySchema) -> Response:
        """
        GET запрос на получение списка операций по счету
        :param query: словарь с accountId (идентификатор счета)
        :return: объект httpx.Response со списком операций
        """
        return self.get('/api/v1/operations', params=QueryParams(**query.model_dump(by_alias=True)))

    def get_operations(self, account_id: str) -> GetOperationsResponseSchema:
        """
        Получение операций по счету
        :param account_id: идентификатор счета
        :return: ответ запроса в json(словарь со списком операций по счету)
        """
        query = GetOperationsQuerySchema(account_id=account_id)
        response = self.get_operations_api(query)
        return GetOperationsResponseSchema.model_validate_json(response.text)

    def get_operations_summary_api(self, query: GetOperationsSummaryQuerySchema) -> Response:
        """
        GET запрос на получение сводной информации по операциям счета
        :param query: словарь с accountId (идентификатор счета)
        :return: объект httpx.Response со сводной информацией по операциям
        """
        return self.get('/api/v1/operations/operations-summary', params=QueryParams(**query.model_dump(by_alias=True)))

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseSchema:
        """
        Получение краткой информации операций по счету
        :param account_id: идентификатор счета
        :return: ответ запроса в json(словарь со списком краткой информации операций по счету)
        """
        query = GetOperationsSummaryQuerySchema(account_id=account_id)
        response = self.get_operations_summary_api(query)
        return GetOperationsSummaryResponseSchema.model_validate_json(response.text)

    def get_operations_receipt_api(self, operation_id: str) -> Response:
        """
        GET запрос на получение квитанции об операции
        :param operation_id: идентификатор операции
        :return: объект httpx.Response с данными квитанции (включая url на скачивание)
        """
        return self.get(f'/api/v1/operations/operation-receipt/{operation_id}')

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseSchema:
        """
        Получение квитанции по выполненой операции
        :param operation_id: идентификатор операции
        :return: ответ запроса и ссылка на квитанцию
        """
        response = self.get_operations_receipt_api(operation_id)
        return GetOperationReceiptResponseSchema.model_validate_json(response.text)

    def get_operation_api(self, operation_id: str) -> Response:
        """
        GET запрос на получение операции по ее идентификатору
        :param operation_id: идентификатор операции
        :return: объект httpx.Response с данными операции
        """
        return self.get(f'/api/v1/operations/{operation_id}')

    def get_operation(self, operation_id: str) -> GetOperationResponseSchema:
        """
        Получение операции по счету
        :param operation_id: идентификатор операции
        :return: ответ по запросу в json
        """
        response = self.get_operation_api(operation_id)
        return GetOperationResponseSchema.model_validate_json(response.text)

    def make_fee_operation_api(self, request: MakeFeeOperationRequestSchema) -> Response:
        """
        POST запрос на создание операции комиссии
        :param request: словарь с данными операции (status, amount, cardId, accountId)
        :return: объект httpx.Response с данными созданной операции
        """
        return self.post('/api/v1/operations/make-fee-operation', json=request.model_dump(by_alias=True))

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseSchema:
        """
        Создание операции комиссии
        :param account_id: идентификатор счета
        :param card_id: идентификатор карты
        :return: словарь с данными открытого счета
        """
        request = MakeFeeOperationRequestSchema(
            status=BaseOperationStatus.COMPLETED,
            amount=55.77,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_fee_operation_api(request)
        return MakeFeeOperationResponseSchema.model_validate_json(response.text)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestSchema) -> Response:
        """
        POST запрос на создание операции пополнения
        :param request: словарь с данными операции (status, amount, cardId, accountId)
        :return: объект httpx.Response с данными созданной операции
        """
        return self.post('/api/v1/operations/make-top-up-operation', json=request.model_dump(by_alias=True))

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponseSchema:
        """
        создание операции пополнения
        :param account_id: идентификатор счета
        :param card_id: идентификатор карты
        :return: объект httpx.Response с данными созданной операции
        """
        request = MakeTopUpOperationRequestSchema(
            status=BaseOperationStatus.COMPLETED,
            amount=55.77,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_top_up_operation_api(request)
        return MakeTopUpOperationResponseSchema.model_validate_json(response.text)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestSchema) -> Response:
        """
        POST запрос на создание операции кэшбэка
        :param request: словарь с данными операции (status, amount, cardId, accountId)
        :return: объект httpx.Response с данными созданной операции
        """
        return self.post('/api/v1/operations/make-cashback-operation', json=request.model_dump(by_alias=True))

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponseSchema:
        """
        создание операции пополнения
        :param account_id: идентификатор счета
        :param card_id: идентификатор карты
        :return: объект httpx.Response с данными созданной операции
        """
        request = MakeCashbackOperationRequestSchema(
            status=BaseOperationStatus.COMPLETED,
            amount=55.77,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_cashback_operation_api(request)
        return MakeCashbackOperationResponseSchema.model_validate_json(response.text)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestSchema) -> Response:
        """
        POST запрос на создание операции перевода
        :param request: словарь с данными операции (status, amount, cardId, accountId)
        :return: объект httpx.Response с данными созданной операции
        """
        return self.post('/api/v1/operations/make-transfer-operation', json=request.model_dump(by_alias=True))

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponseSchema:
        """
        создание операции перевода
        :param account_id: идентификатор счета
        :param card_id: идентификатор карты
        :return: объект httpx.Response с данными созданной операции
        """
        request = MakeTransferOperationRequestSchema(
            status=BaseOperationStatus.COMPLETED,
            amount=55.77,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_transfer_operation_api(request)
        return MakeTransferOperationResponseSchema.model_validate_json(response.text)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestSchema) -> Response:
        """
        POST запрос на создание операции покупки
        :param request: словарь с данными операции (status, amount, cardId, accountId, category)
        :return: объект httpx.Response с данными созданной операции
        """
        return self.post('/api/v1/operations/make-purchase-operation', json=request.model_dump(by_alias=True))

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchaseOperationResponseSchema:
        """
        создание операции покупки
        :param account_id: идентификатор счета
        :param card_id: идентификатор карты
        :return: объект httpx.Response с данными созданной операции
        """
        request = MakePurchaseOperationRequestSchema(
            status=BaseOperationStatus.COMPLETED,
            amount=55.77,
            card_id=card_id,
            account_id=account_id,
            category='taxi'
        )
        response = self.make_purchase_operation_api(request)
        return MakePurchaseOperationResponseSchema.model_validate_json(response.text)

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestSchema) -> Response:
        """
        POST запрос на создание операции оплаты по счету
        :param request: словарь с данными операции (status, amount, cardId, accountId)
        :return: объект httpx.Response с данными созданной операции
        """
        return self.post('/api/v1/operations/make-bill-payment-operation', json=request.model_dump(by_alias=True))

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponseSchema:
        """
        создание операции оплаты по счету
        :param account_id: идентификатор счета
        :param card_id: идентификатор карты
        :return: объект httpx.Response с данными созданной операции
        """
        request = MakeBillPaymentOperationRequestSchema(
            status=BaseOperationStatus.COMPLETED,
            amount=55.77,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_bill_payment_operation_api(request)
        return MakeBillPaymentOperationResponseSchema.model_validate_json(response.text)

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestSchema) -> Response:
        """
        POST запрос на создание операции снятия наличных денег
        :param request: словарь с данными операции (status, amount, cardId, accountId)
        :return: объект httpx.Response с данными созданной операции
        """
        return self.post('/api/v1/operations/make-cash-withdrawal-operation', json=request.model_dump(by_alias=True))

    def make_cash_withdrawal_operation(self, card_id: str,
                                       account_id: str) -> MakeCashWithdrawalOperationResponseSchema:
        """
        создание операции снятия наличных денег
        :param account_id: идентификатор счета
        :param card_id: идентификатор карты
        :return: объект httpx.Response с данными созданной операции
        """
        request = MakeCashWithdrawalOperationRequestSchema(
            status=BaseOperationStatus.COMPLETED,
            amount=55.77,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return MakeCashWithdrawalOperationResponseSchema.model_validate_json(response.text)


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создает экземпляр OperationsGatewayHTTPClient с настроенным HTTPClient
    :return: Готовый к использованию OperationsGatewayHTTPClient
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
