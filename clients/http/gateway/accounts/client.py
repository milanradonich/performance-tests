from typing import TypedDict

from httpx import Response, QueryParams

from clients.http.client import HTTPClient


class GetAccountsQueryDict(TypedDict):
    """
    структура для получения списка счетов
    """
    userId: str


class OpenDepositAccountRequestDict(TypedDict):
    """
    структура для открытия депозитного счета
    """
    userId: str


class OpenSavingsAccountRequestDict(TypedDict):
    """
    структура для открытия сберегательного счета
    """
    userId: str


class OpenDebitCardAccountRequestDict(TypedDict):
    """
    структура для открытия дебетового счета
    """
    userId: str


class OpenCreditCardAccountRequestDict(TypedDict):
    """
    структура для открытия кредитного счета
    """
    userId: str


class AccountsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/accounts
    """

    def get_accounts_api(self, query: GetAccountsQueryDict) -> Response:
        """
        Get запрос для получения списка счетов пользователя
        :param query: словарь (userId: '1234'
        :return: объект response c данными о счетах
        """
        return self.get("/api/v1/accounts", params=QueryParams(**query))

    def open_deposit_account_api(self, request: OpenDepositAccountRequestDict) -> Response:
        """
        POST запрос на открытие депозитного счета
        :param request: словарь с userId
        :return: response с результатом запроса
        """
        return self.post("/api/v1/accounts/open-deposit-account", json=request)

    def open_savings_account_api(self, request: OpenSavingsAccountRequestDict) -> Response:
        """
        POST запрос на открытие сберегательного счета
        :param request: словарь с userId
        :return: response с результатом запроса
        """
        return self.post("/api/v1/accounts/open-savings-account", json=request)

    def open_debit_card_account_api(self, request: OpenDebitCardAccountRequestDict) -> Response:
        """
        POST запрос на открытие дебетового счета
        :param request: словарь с userId
        :return: response с результатом запроса
        """
        return self.post("/api/v1/accounts/open-debit-card-account", json=request)

    def open_credit_card_account_api(self, request: OpenCreditCardAccountRequestDict) -> Response:
        """
        POST запрос на открытие кредитного счета
        :param request: словарь с userId
        :return: response с результатом запроса
        """
        return self.post("/api/v1/accounts/open-credit-card-account", json=request)
