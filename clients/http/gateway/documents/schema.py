from pydantic import BaseModel


class DocumentSchema(BaseModel):
    """
    Структура ответа получения документов
    """
    url: str
    document: str


class GetTariffDocumentResponseSchema(BaseModel):
    """Структура ответа на получение документа по тарифу"""

    tariff: DocumentSchema


class GetContractDocumentResponseSchema(BaseModel):
    """Структура ответа на получение документа по контракту"""

    contract: DocumentSchema
