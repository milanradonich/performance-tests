from typing import TypedDict

from httpx import Response, QueryParams

from clients.http.client import HTTPClient
from clients.http.gateway.cards.client import CardDict
from clients.http.gateway.client import build_gateway_http_client


class AccountDict(TypedDict):
    """
    Структура данных счета
    """
    id: str
    type: str
    cards: list[CardDict]
    status: str
    balance: float


class GetAccountsResponseDict(TypedDict):
    """
    Структура ответа на получение списка счетов
    """
    accounts: list[AccountDict]


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


class OpenDepositAccountResponseDict(TypedDict):
    """
    Структура ответа на открытие депозитного счета
    """
    account: AccountDict


class OpenSavingsAccountRequestDict(TypedDict):
    """
    структура для открытия сберегательного счета
    """
    userId: str


class OpenDSavingsAccountResponseDict(TypedDict):
    """
    Структура ответа на открытие сберегательного счета
    """
    account: AccountDict


class OpenDebitCardAccountRequestDict(TypedDict):
    """
    структура для открытия дебетового счета
    """
    userId: str


class OpenDebitCardAccountResponseDict(TypedDict):
    """
    Структура ответа на открытие дебетового счета
    """
    account: AccountDict


class OpenCreditCardAccountRequestDict(TypedDict):
    """
    структура для открытия кредитного счета
    """
    userId: str


class OpenCreditCardAccountResponseDict(TypedDict):
    """
    Структура ответа на открытие кредитного счета
    """
    account: AccountDict


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

    def get_accounts(self, user_id: str) -> GetAccountsResponseDict:
        """
        Получает список счетов пользователя
        :param user_id: идентификатор пользователя
        :return: словарь со списком счетов пользователя
        """
        query = GetAccountsQueryDict(userId=user_id)
        response = self.get_accounts_api(query)
        return response.json()

    def open_deposit_account(self, user_id: str) -> OpenDepositAccountResponseDict:
        """
        Открывает депозитный счет пользователю
        :param user_id: идентификатор пользователя
        :return: словарь с данными открытого счета
        """
        request = OpenDepositAccountRequestDict(userId=user_id)
        response = self.open_deposit_account_api(request)
        return response.json()

    def open_savings_account(self, user_id: str) -> OpenDSavingsAccountResponseDict:
        """
        Открывает сберегательный счет пользователю
        :param user_id: идентификатор пользователя
        :return: словарь с данными открытого счета
        """
        request = OpenSavingsAccountRequestDict(userId=user_id)
        response = self.open_savings_account_api(request)
        return response.json()

    def open_debit_card_account(self, user_id: str) -> OpenDebitCardAccountResponseDict:
        """
        Открывает дебетовый счет пользователю
        :param user_id: идентификатор пользователя
        :return: словарь с данными открытого счета
        """
        request = OpenDebitCardAccountRequestDict(userId=user_id)
        response = self.open_debit_card_account_api(request)
        return response.json()

    def open_credit_card_account(self, user_id: str) -> OpenCreditCardAccountResponseDict:
        """
        Открывает кредитный счет пользователю
        :param user_id: идентификатор пользователя
        :return: словарь с данными открытого счета
        """
        request = OpenCreditCardAccountRequestDict(userId=user_id)
        response = self.open_credit_card_account_api(request)
        return response.json()


def build_accounts_gateway_http_client() -> AccountsGatewayHTTPClient:
    """
    Функция создает экземпляр AccountsGatewayHTTPClient с настроенным HTTPClient
    :return: Готовый к использованию AccountsGatewayHTTPClient
    """
    return AccountsGatewayHTTPClient(client=build_gateway_http_client())