from pydantic import BaseModel, EmailStr, Field, ConfigDict


class UserSchema(BaseModel):
    """
    Структура данных пользователя
    """
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    phone_number: str = Field(alias="phoneNumber")


class GetUserResponseSchema(BaseModel):
    """
    Структура ответа на получение пользователя
    """
    user: UserSchema


class CreateUserRequestSchema(BaseModel):
    """
    Структура запроса на создание пользователя
    """
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    phone_number: str = Field(alias="phoneNumber")


class CreateUserResponseSchema(BaseModel):
    """
    Структура ответа на создание пользователя
    """
    user: UserSchema
