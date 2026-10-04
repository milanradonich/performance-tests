from pydantic import BaseModel, EmailStr, ConfigDict
from pydantic.alias_generators import to_camel


class CreateUserRequestSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
    email: EmailStr
    last_name: str
    first_name: str
    middle_name: str
    phone_number: str


class UserSchema(CreateUserRequestSchema):
    id: str


class CreateUserResponseSchema(BaseModel):
    user: UserSchema
