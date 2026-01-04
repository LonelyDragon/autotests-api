from pydantic import BaseModel, Field, EmailStr, ConfigDict

from tools.fakers import fake


class UserSchema(BaseModel):
    """Струтура объекта пользователь"""
    id: str
    email: EmailStr
    first_name: str = str
    last_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserRequestSchema(BaseModel):
    """Структура запроса на создание пользователя /api/v1/users"""
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)
    last_name: str = Field(alias="lastName", default_factory=fake.last_name)
    first_name: str = Field(alias="firstName", default_factory=fake.first_name)
    middle_name: str = Field(alias="middleName", default_factory=fake.middle_name)


class CreateUserResponseSchema(BaseModel):
    """Струтура ответа на запрос о создании пользователя /api/v1/users"""
    user: UserSchema
