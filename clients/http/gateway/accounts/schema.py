from pydantic import BaseModel, Field, ConfigDict

from clients.http.gateway.cards.schema import CardSchema
from enum import StrEnum


class AccountType(StrEnum):
    DEPOSIT = "DEPOSIT"
    SAVINGS = "SAVINGS"
    DEBIT_CARD = "DEBIT_CARD"
    CREDIT_CARD = "CREDIT_CARD"


class AccountStatus(StrEnum):
    ACTIVE = "ACTIVE"
    CLOSED = "CLOSED"
    PENDING_CLOSURE = "PENDING_CLOSURE"


class AccountSchema(BaseModel):
    """
    Структура данных счета
    """
    id: str
    type: AccountType
    cards: list[CardSchema]
    status: AccountStatus
    balance: float


class GetAccountsResponseSchema(BaseModel):
    """
    Структура ответа на получение списка счетов
    """
    accounts: list[AccountSchema]


class GetAccountsQuerySchema(BaseModel):
    """
    структура для получения списка счетов
    """
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias="userId")


class OpenDepositAccountRequestSchema(BaseModel):
    """
    структура для открытия депозитного счета
    """
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias="userId")


class OpenDepositAccountResponseSchema(BaseModel):
    """
    Структура ответа на открытие депозитного счета
    """
    account: AccountSchema


class OpenSavingsAccountRequestSchema(BaseModel):
    """
    структура для открытия сберегательного счета
    """
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias="userId")


class OpenDSavingsAccountResponseSchema(BaseModel):
    """
    Структура ответа на открытие сберегательного счета
    """
    account: AccountSchema


class OpenDebitCardAccountRequestSchema(BaseModel):
    """
    структура для открытия дебетового счета
    """
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias="userId")


class OpenDebitCardAccountResponseSchema(BaseModel):
    """
    Структура ответа на открытие дебетового счета
    """
    account: AccountSchema


class OpenCreditCardAccountRequestSchema(BaseModel):
    """
    структура для открытия кредитного счета
    """
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias="userId")


class OpenCreditCardAccountResponseSchema(BaseModel):
    """
    Структура ответа на открытие кредитного счета
    """
    account: AccountSchema
