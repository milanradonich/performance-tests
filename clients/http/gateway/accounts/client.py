from httpx import Response, QueryParams

from clients.http.client import HTTPClient
from clients.http.gateway.accounts.schema import GetAccountsQuerySchema, OpenDepositAccountRequestSchema, \
    OpenSavingsAccountRequestSchema, OpenDebitCardAccountRequestSchema, OpenCreditCardAccountRequestSchema, \
    GetAccountsResponseSchema, OpenDepositAccountResponseSchema, OpenDSavingsAccountResponseSchema, \
    OpenDebitCardAccountResponseSchema, OpenCreditCardAccountResponseSchema
from clients.http.gateway.client import build_gateway_http_client


class AccountsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/accounts
    """

    def get_accounts_api(self, query: GetAccountsQuerySchema) -> Response:
        """
        Get запрос для получения списка счетов пользователя
        :param query: словарь (userId: '1234'
        :return: объект response c данными о счетах
        """
        return self.get("/api/v1/accounts", params=QueryParams(**query.model_dump(by_alias=True)))

    def open_deposit_account_api(self, request: OpenDepositAccountRequestSchema) -> Response:
        """
        POST запрос на открытие депозитного счета
        :param request: словарь с userId
        :return: response с результатом запроса
        """
        return self.post("/api/v1/accounts/open-deposit-account", json=request.model_dump(by_alias=True))

    def open_savings_account_api(self, request: OpenSavingsAccountRequestSchema) -> Response:
        """
        POST запрос на открытие сберегательного счета
        :param request: словарь с userId
        :return: response с результатом запроса
        """
        return self.post("/api/v1/accounts/open-savings-account", json=request.model_dump(by_alias=True))

    def open_debit_card_account_api(self, request: OpenDebitCardAccountRequestSchema) -> Response:
        """
        POST запрос на открытие дебетового счета
        :param request: словарь с userId
        :return: response с результатом запроса
        """
        return self.post("/api/v1/accounts/open-debit-card-account", json=request.model_dump(by_alias=True))

    def open_credit_card_account_api(self, request: OpenCreditCardAccountRequestSchema) -> Response:
        """
        POST запрос на открытие кредитного счета
        :param request: словарь с userId
        :return: response с результатом запроса
        """
        return self.post("/api/v1/accounts/open-credit-card-account", json=request.model_dump(by_alias=True))

    def get_accounts(self, user_id: str) -> GetAccountsResponseSchema:
        """
        Получает список счетов пользователя
        :param user_id: идентификатор пользователя
        :return: словарь со списком счетов пользователя
        """
        query = GetAccountsQuerySchema(user_id=user_id)
        response = self.get_accounts_api(query)
        return GetAccountsResponseSchema.model_validate_json(response.text)

    def open_deposit_account(self, user_id: str) -> OpenDepositAccountResponseSchema:
        """
        Открывает депозитный счет пользователю
        :param user_id: идентификатор пользователя
        :return: словарь с данными открытого счета
        """
        request = OpenDepositAccountRequestSchema(user_id=user_id)
        response = self.open_deposit_account_api(request)
        return OpenDepositAccountResponseSchema.model_validate_json(response.text)

    def open_savings_account(self, user_id: str) -> OpenDSavingsAccountResponseSchema:
        """
        Открывает сберегательный счет пользователю
        :param user_id: идентификатор пользователя
        :return: словарь с данными открытого счета
        """
        request = OpenSavingsAccountRequestSchema(user_id=user_id)
        response = self.open_savings_account_api(request)
        return OpenDSavingsAccountResponseSchema.model_validate_json(response.text)

    def open_debit_card_account(self, user_id: str) -> OpenDebitCardAccountResponseSchema:
        """
        Открывает дебетовый счет пользователю
        :param user_id: идентификатор пользователя
        :return: словарь с данными открытого счета
        """
        request = OpenDebitCardAccountRequestSchema(user_id=user_id)
        response = self.open_debit_card_account_api(request)
        return OpenDebitCardAccountResponseSchema.model_validate_json(response.text)

    def open_credit_card_account(self, user_id: str) -> OpenCreditCardAccountResponseSchema:
        """
        Открывает кредитный счет пользователю
        :param user_id: идентификатор пользователя
        :return: словарь с данными открытого счета
        """
        request = OpenCreditCardAccountRequestSchema(user_id=user_id)
        response = self.open_credit_card_account_api(request)
        return OpenCreditCardAccountResponseSchema.model_validate_json(response.text)


def build_accounts_gateway_http_client() -> AccountsGatewayHTTPClient:
    """
    Функция создает экземпляр AccountsGatewayHTTPClient с настроенным HTTPClient
    :return: Готовый к использованию AccountsGatewayHTTPClient
    """
    return AccountsGatewayHTTPClient(client=build_gateway_http_client())