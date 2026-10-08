from pydantic import BaseModel, Field, ConfigDict
from enum import StrEnum, IntEnum


class CardType(StrEnum):
    VIRTUAL = "VIRTUAL"
    PHYSICAL = "PHYSICAL"


class CardStatus(StrEnum):
    ACTIVE = "ACTIVE"
    FROZEN = "FROZEN"
    CLOSED = "CLOSED"
    BLOCKED = "BLOCKED"


class CardPaymentSystem(StrEnum):
    VISA = "VISA"
    MASTERCARD = "MASTERCARD"


class CardSchema(BaseModel):
    """
    Структура данных карты
    """
    id: str
    pin: str
    cvv: str
    type: CardType
    status: CardStatus
    account_id: str = Field(alias="accountId")
    card_number: str = Field(alias="cardNumber")
    card_holder: str = Field(alias="cardHolder")
    expiry_date: str = Field(alias="expiryDate")
    payment_system: CardPaymentSystem = Field(alias="paymentSystem")


class IssueVirtualCardRequestSchema(BaseModel):
    """
    Структура запроса на выпуск виртуальной карты
    """
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias="userId")
    account_id: str = Field(alias="accountId")


class IssuePhysicalCardRequestSchema(BaseModel):
    """
    Структура запроса на выпуск физической карты
    """
    model_config = ConfigDict(populate_by_name=True)

    user_id: str = Field(alias="userId")
    account_id: str = Field(alias="accountId")


class IssuePhysicalCardResponseSchema(BaseModel):
    """
    Структура ответа на выпуск физической карты
    """
    card: CardSchema


class IssueVirtualCardResponseSchema(BaseModel):
    """
    Структура ответа на выпуск виртуальной карты
    """
    card: CardSchema