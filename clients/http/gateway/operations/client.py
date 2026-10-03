from typing import TypedDict

from httpx import Response, QueryParams

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


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


class BaseMakeOperationRequestDict(TypedDict):
    """
    Базовая структура запроса на создание операции
    """
    status: str
    amount: float
    cardId: str
    accountId: str


class MakeFeeOperationRequestDict(BaseMakeOperationRequestDict):
    """
    Структура для создания операции комиссии
    """


class MakeTopUpOperationRequestDict(BaseMakeOperationRequestDict):
    """
    Структура для создания операции пополнения
    """


class MakeCashbackOperationRequestDict(BaseMakeOperationRequestDict):
    """
    Структура для создания операции кэшбэка
    """


class MakeTransferOperationRequestDict(BaseMakeOperationRequestDict):
    """
    Структура для создания операции перевода
    """


class MakePurchaseOperationRequestDict(BaseMakeOperationRequestDict):
    """
    Структура для создания операции покупки
    """
    category: str


class MakeBillPaymentOperationRequestDict(BaseMakeOperationRequestDict):
    """
    Структура для создания операции оплаты по счету
    """


class MakeCashWithdrawalOperationRequestDict(BaseMakeOperationRequestDict):
    """
    Структура для создания операции снятия наличных денег
    """


class OperationDict(TypedDict):
    """Структура данных операции"""
    id: str
    type: str
    status: str
    amount: float
    cardId: str
    category: str
    createdAt: str
    accountId: str


class GetOperationsResponseDict(TypedDict):
    """
    Структура ответа на получение операций
    """
    operations: list[OperationDict]


class OperationSummaryDict(TypedDict):
    """
    Структура короткой информации по операции
    """
    spentAmount: float
    receivedAmount: float
    cashbackAmount: float


class GetOperationsSummaryResponseDict(TypedDict):
    """
    Структура ответа на получение короткой информации по операциям
    """
    summary: OperationSummaryDict


class ReceiptDict(TypedDict):
    """
    Структура отвта по получению квитанции об операции
    """
    url: str
    document: str


class GetOperationReceiptResponseDict(TypedDict):
    """Структура ответа получаения квитанции"""
    receipt: ReceiptDict


class GetOperationResponseDict(TypedDict):
    """Структура ответа по информации об операции"""
    operation: OperationDict


class MakeFeeOperationResponseDict(TypedDict):
    """Стурктура ответа по созданию операции комиссии"""
    operation: OperationDict


class MakeTopUpOperationResponseDict(TypedDict):
    """Стурктура ответа по созданию операции пополнения"""
    operation: OperationDict


class MakeCashbackOperationResponseDict(TypedDict):
    """Стурктура ответа по созданию операции кэшбека"""
    operation: OperationDict


class MakeTransferOperationResponseDict(TypedDict):
    """Стурктура ответа по созданию операции перевода"""
    operation: OperationDict


class MakePurchaseOperationResponseDict(TypedDict):
    """Стурктура ответа по созданию операции покупки"""
    operation: OperationDict


class MakeBillPaymentOperationResponseDict(TypedDict):
    """Стурктура ответа по созданию операции оплаты по счету"""
    operation: OperationDict


class MakeCashWithdrawalOperationResponseDict(TypedDict):
    """Структура ответа по созданию операции снятия наличных денег"""
    operation: OperationDict


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

    def get_operations(self, account_id: str) -> GetOperationsResponseDict:
        """
        Получение операций по счету
        :param account_id: идентификатор счета
        :return: ответ запроса в json(словарь со списком операций по счету)
        """
        query = GetOperationsQueryDict(accountId=account_id)
        response = self.get_operations_api(query)
        return response.json()

    def get_operations_summary_api(self, query: GetOperationsSummaryQueryDict) -> Response:
        """
        GET запрос на получение сводной информации по операциям счета
        :param query: словарь с accountId (идентификатор счета)
        :return: объект httpx.Response со сводной информацией по операциям
        """
        return self.get('/api/v1/operations/operations-summary', params=QueryParams(**query))

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseDict:
        """
        Получение краткой информации операций по счету
        :param account_id: идентификатор счета
        :return: ответ запроса в json(словарь со списком краткой информации операций по счету)
        """
        query = GetOperationsSummaryQueryDict(accountId=account_id)
        response = self.get_operations_summary_api(query)
        return response.json()

    def get_operations_receipt_api(self, operation_id: str) -> Response:
        """
        GET запрос на получение квитанции об операции
        :param operation_id: идентификатор операции
        :return: объект httpx.Response с данными квитанции (включая url на скачивание)
        """
        return self.get(f'/api/v1/operations/operation-receipt/{operation_id}')

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseDict:
        """
        Получение квитанции по выполненой операции
        :param operation_id: идентификатор операции
        :return: ответ запроса и ссылка на квитанцию
        """
        response = self.get_operations_receipt_api(operation_id)
        return response.json()

    def get_operation_api(self, operation_id: str) -> Response:
        """
        GET запрос на получение операции по ее идентификатору
        :param operation_id: идентификатор операции
        :return: объект httpx.Response с данными операции
        """
        return self.get(f'/api/v1/operations/{operation_id}')

    def get_operation(self, operation_id: str) -> GetOperationResponseDict:
        """
        Получение операции по счету
        :param operation_id: идентификатор операции
        :return: ответ по запросу в json
        """
        response = self.get_operation_api(operation_id)
        return response.json()

    def make_fee_operation_api(self, request: MakeFeeOperationRequestDict) -> Response:
        """
        POST запрос на создание операции комиссии
        :param request: словарь с данными операции (status, amount, cardId, accountId)
        :return: объект httpx.Response с данными созданной операции
        """
        return self.post('/api/v1/operations/make-fee-operation', json=request)

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseDict:
        """
        Создание операции комиссии
        :param account_id: идентификатор счета
        :param card_id: идентификатор карты
        :return: словарь с данными открытого счета
        """
        request = MakeFeeOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_fee_operation_api(request)
        return response.json()

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequestDict) -> Response:
        """
        POST запрос на создание операции пополнения
        :param request: словарь с данными операции (status, amount, cardId, accountId)
        :return: объект httpx.Response с данными созданной операции
        """
        return self.post('/api/v1/operations/make-top-up-operation', json=request)

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponseDict:
        """
        создание операции пополнения
        :param account_id: идентификатор счета
        :param card_id: идентификатор карты
        :return: объект httpx.Response с данными созданной операции
        """
        request = MakeTopUpOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_top_up_operation_api(request)
        return response.json()

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequestDict) -> Response:
        """
        POST запрос на создание операции кэшбэка
        :param request: словарь с данными операции (status, amount, cardId, accountId)
        :return: объект httpx.Response с данными созданной операции
        """
        return self.post('/api/v1/operations/make-cashback-operation', json=request)

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponseDict:
        """
        создание операции пополнения
        :param account_id: идентификатор счета
        :param card_id: идентификатор карты
        :return: объект httpx.Response с данными созданной операции
        """
        request = MakeCashbackOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cashback_operation_api(request)
        return response.json()

    def make_transfer_operation_api(self, request: MakeTransferOperationRequestDict) -> Response:
        """
        POST запрос на создание операции перевода
        :param request: словарь с данными операции (status, amount, cardId, accountId)
        :return: объект httpx.Response с данными созданной операции
        """
        return self.post('/api/v1/operations/make-transfer-operation', json=request)

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponseDict:
        """
        создание операции перевода
        :param account_id: идентификатор счета
        :param card_id: идентификатор карты
        :return: объект httpx.Response с данными созданной операции
        """
        request = MakeTransferOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_transfer_operation_api(request)
        return response.json()

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequestDict) -> Response:
        """
        POST запрос на создание операции покупки
        :param request: словарь с данными операции (status, amount, cardId, accountId, category)
        :return: объект httpx.Response с данными созданной операции
        """
        return self.post('/api/v1/operations/make-purchase-operation', json=request)

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchaseOperationResponseDict:
        """
        создание операции покупки
        :param account_id: идентификатор счета
        :param card_id: идентификатор карты
        :return: объект httpx.Response с данными созданной операции
        """
        request = MakePurchaseOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id,
            category='taxi'
        )
        response = self.make_purchase_operation_api(request)
        return response.json()

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequestDict) -> Response:
        """
        POST запрос на создание операции оплаты по счету
        :param request: словарь с данными операции (status, amount, cardId, accountId)
        :return: объект httpx.Response с данными созданной операции
        """
        return self.post('/api/v1/operations/make-bill-payment-operation', json=request)

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponseDict:
        """
        создание операции оплаты по счету
        :param account_id: идентификатор счета
        :param card_id: идентификатор карты
        :return: объект httpx.Response с данными созданной операции
        """
        request = MakeBillPaymentOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_bill_payment_operation_api(request)
        return response.json()

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequestDict) -> Response:
        """
        POST запрос на создание операции снятия наличных денег
        :param request: словарь с данными операции (status, amount, cardId, accountId)
        :return: объект httpx.Response с данными созданной операции
        """
        return self.post('/api/v1/operations/make-cash-withdrawal-operation', json=request)

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> MakeCashWithdrawalOperationResponseDict:
        """
        создание операции снятия наличных денег
        :param account_id: идентификатор счета
        :param card_id: идентификатор карты
        :return: объект httpx.Response с данными созданной операции
        """
        request = MakeCashWithdrawalOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return response.json()


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создает экземпляр OperationsGatewayHTTPClient с настроенным HTTPClient
    :return: Готовый к использованию OperationsGatewayHTTPClient
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
