from pydantic import BaseModel, Field, EmailStr, ConfigDict


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

    email: EmailStr
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserResponseSchema(BaseModel):
    """Струтура ответа на запрос о создании пользователя /api/v1/users"""
    user: UserSchema
