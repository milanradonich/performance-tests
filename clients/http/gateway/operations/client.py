from typing import TypedDict

from httpx import Response, QueryParams

from clients.http.client import HTTPClient


class BaseOperationsQueryDict(TypedDict):
    """
    Базовая структура query-параметров для запросов операций по счету
    """
    accountId: str


class GetOperationsQueryDict(BaseOperationsQueryDict):
    """
    Структура для получения списка операций
    """


class GetOperationsSummaryQueryDict(BaseOperationsQueryDict):
    """
    Структура для получения сводной информации по операциям
    """


class BaseCreateOperationRequestDict(TypedDict):
    """
    Базовая структура запроса на создание операции
    """
    status: str
    amount: int
    cardId: str
    accountId: str


class CreateOperationFeeRequestDict(BaseCreateOperationRequestDict):
    """
    Структура для создания операции комиссии
    """


class CreateOperationTopUpRequestDict(BaseCreateOperationRequestDict):
    """
    Структура для создания операции пополнения
    """


class CreateOperationCashbackRequestDict(BaseCreateOperationRequestDict):
    """
    Структура для создания операции кэшбэка
    """


class CreateOperationTransferRequestDict(BaseCreateOperationRequestDict):
    """
    Структура для создания операции перевода
    """


class CreateOperationPurchaseRequestDict(BaseCreateOperationRequestDict):
    """
    Структура для создания операции покупки
    """
    category: str


class CreateOperationBillPaymentRequestDict(BaseCreateOperationRequestDict):
    """
    Структура для создания операции оплаты по счету
    """


class CreateOperationCashWithdrawalRequestDict(BaseCreateOperationRequestDict):
    """
    Структура для создания операции снятия наличных денег
    """


class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations
    """
    def get_operations_api(self, query: GetOperationsQueryDict) -> Response:
        """
        GET запрос на получение списка операций по счету
        :param query: словарь с accountId (идентификатор счета)
        :return: объект httpx.Response со списком операций
        """
        return self.get('/api/v1/operations', params=QueryParams(**query))

    def get_operations_summary_api(self, query: GetOperationsSummaryQueryDict) -> Response:
        """
        GET запрос на получение сводной информации по операциям счета
        :param query: словарь с accountId (идентификатор счета)
        :return: объект httpx.Response со сводной информацией по операциям
        """
        return self.get('/api/v1/operations/operations-summary', params=QueryParams(**query))

    def get_operations_receipt_api(self, operation_id: str) -> Response:
        """
        GET запрос на получение квитанции об операции
        :param operation_id: идентификатор операции
        :return: объект httpx.Response с данными квитанции (включая url на скачивание)
        """
        return self.get(f'/api/v1/operations/operation-receipt/{operation_id}')

    def get_operation_api(self, operation_id: str) -> Response:
        """
        GET запрос на получение операции по ее идентификатору
        :param operation_id: идентификатор операции
        :return: объект httpx.Response с данными операции
        """
        return self.get(f'/api/v1/operations/{operation_id}')

    def make_fee_operation_api(self, request: CreateOperationFeeRequestDict) -> Response:
        """
        POST запрос на создание операции комиссии
        :param request: словарь с данными операции (status, amount, cardId, accountId)
        :return: объект httpx.Response с данными созданной операции
        """
        return self.post('/api/v1/operations/make-fee-operation', json=request)

    def make_top_up_operation_api(self, request: CreateOperationTopUpRequestDict) -> Response:
        """
        POST запрос на создание операции пополнения
        :param request: словарь с данными операции (status, amount, cardId, accountId)
        :return: объект httpx.Response с данными созданной операции
        """
        return self.post('/api/v1/operations/make-top-up-operation', json=request)

    def make_cashback_operation_api(self, request: CreateOperationCashbackRequestDict) -> Response:
        """
        POST запрос на создание операции кэшбэка
        :param request: словарь с данными операции (status, amount, cardId, accountId)
        :return: объект httpx.Response с данными созданной операции
        """
        return self.post('/api/v1/operations/make-cashback-operation', json=request)

    def make_transfer_operation_api(self, request: CreateOperationTransferRequestDict) -> Response:
        """
        POST запрос на создание операции перевода
        :param request: словарь с данными операции (status, amount, cardId, accountId)
        :return: объект httpx.Response с данными созданной операции
        """
        return self.post('/api/v1/operations/make-transfer-operation', json=request)

    def make_purchase_operation_api(self, request: CreateOperationPurchaseRequestDict) -> Response:
        """
        POST запрос на создание операции покупки
        :param request: словарь с данными операции (status, amount, cardId, accountId, category)
        :return: объект httpx.Response с данными созданной операции
        """
        return self.post('/api/v1/operations/make-purchase-operation', json=request)

    def make_bill_payment_operation_api(self, request: CreateOperationBillPaymentRequestDict) -> Response:
        """
        POST запрос на создание операции оплаты по счету
        :param request: словарь с данными операции (status, amount, cardId, accountId)
        :return: объект httpx.Response с данными созданной операции
        """
        return self.post('/api/v1/operations/make-bill-payment-operation', json=request)

    def make_cash_withdrawal_operation_api(self, request: CreateOperationCashWithdrawalRequestDict) -> Response:
        """
        POST запрос на создание операции снятия наличных денег
        :param request: словарь с данными операции (status, amount, cardId, accountId)
        :return: объект httpx.Response с данными созданной операции
        """
        return self.post('/api/v1/operations/make-cash-withdrawal-operation', json=request)
