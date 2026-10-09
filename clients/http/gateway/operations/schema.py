from enum import Enum

from pydantic import BaseModel, Field, ConfigDict


class BaseOperationStatus(str, Enum):
    """Базовый класс статусов операций.
    Используется в запросе по всем операциям и в структуре данных операции"""
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    UNSPECIFIED = "UNSPECIFIED"


class OperationType(str, Enum):
    """Типы операций"""
    FEE = "FEE"
    TOP_UP = "TOP_UP"
    PURCHASE = "PURCHASE"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"


class BaseOperationsQuerySchema(BaseModel):
    """
    Базовая структура query-параметров для запросов операций по счету
    """
    model_config = ConfigDict(populate_by_name=True)

    account_id: str = Field(alias="accountId")


class GetOperationsQuerySchema(BaseOperationsQuerySchema):
    """
    Структура для получения списка операций
    """


class GetOperationsSummaryQuerySchema(BaseOperationsQuerySchema):
    """
    Структура для получения сводной информации по операциям
    """


class BaseMakeOperationRequestSchema(BaseModel):
    """
    Базовая структура запроса на создание операции
    """
    model_config = ConfigDict(populate_by_name=True)

    status: BaseOperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeFeeOperationRequestSchema(BaseMakeOperationRequestSchema):
    """
    Структура для создания операции комиссии
    """


class MakeTopUpOperationRequestSchema(BaseMakeOperationRequestSchema):
    """
    Структура для создания операции пополнения
    """


class MakeCashbackOperationRequestSchema(BaseMakeOperationRequestSchema):
    """
    Структура для создания операции кэшбэка
    """


class MakeTransferOperationRequestSchema(BaseMakeOperationRequestSchema):
    """
    Структура для создания операции перевода
    """


class MakePurchaseOperationRequestSchema(BaseMakeOperationRequestSchema):
    """
    Структура для создания операции покупки
    """
    category: str


class MakeBillPaymentOperationRequestSchema(BaseMakeOperationRequestSchema):
    """
    Структура для создания операции оплаты по счету
    """


class MakeCashWithdrawalOperationRequestSchema(BaseMakeOperationRequestSchema):
    """
    Структура для создания операции снятия наличных денег
    """


class OperationSchema(BaseModel):
    """Структура данных операции"""
    model_config = ConfigDict(populate_by_name=True)

    id: str
    type: OperationType
    status: BaseOperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    category: str
    created_at: str = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")


class GetOperationsResponseSchema(BaseModel):
    """
    Структура ответа на получение операций
    """
    operations: list[OperationSchema]


class OperationSummarySchema(BaseModel):
    """
    Структура короткой информации по операции
    """
    model_config = ConfigDict(populate_by_name=True)

    spent_amount: float = Field(alias="spentAmount")
    received_amount: float = Field(alias="receivedAmount")
    cashback_amount: float = Field(alias="cashbackAmount")


class GetOperationsSummaryResponseSchema(BaseModel):
    """
    Структура ответа на получение короткой информации по операциям
    """
    summary: OperationSummarySchema


class ReceiptSchema(BaseModel):
    """
    Структура отвта по получению квитанции об операции
    """
    url: str
    document: str


class GetOperationReceiptResponseSchema(BaseModel):
    """Структура ответа получаения квитанции"""
    receipt: ReceiptSchema


class GetOperationResponseSchema(BaseModel):
    """Структура ответа по информации об операции"""
    operation: OperationSchema


class MakeFeeOperationResponseSchema(BaseModel):
    """Стурктура ответа по созданию операции комиссии"""
    operation: OperationSchema


class MakeTopUpOperationResponseSchema(BaseModel):
    """Стурктура ответа по созданию операции пополнения"""
    operation: OperationSchema


class MakeCashbackOperationResponseSchema(BaseModel):
    """Стурктура ответа по созданию операции кэшбека"""
    operation: OperationSchema


class MakeTransferOperationResponseSchema(BaseModel):
    """Стурктура ответа по созданию операции перевода"""
    operation: OperationSchema


class MakePurchaseOperationResponseSchema(BaseModel):
    """Стурктура ответа по созданию операции покупки"""
    operation: OperationSchema


class MakeBillPaymentOperationResponseSchema(BaseModel):
    """Стурктура ответа по созданию операции оплаты по счету"""
    operation: OperationSchema


class MakeCashWithdrawalOperationResponseSchema(BaseModel):
    """Структура ответа по созданию операции снятия наличных денег"""
    operation: OperationSchema
