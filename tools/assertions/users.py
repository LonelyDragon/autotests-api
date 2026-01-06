from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, UserSchema, \
    GetUserResponseSchema
from tools.assertions.base import assert_equal


def assert_create_user_response(
        request: CreateUserRequestSchema,
        response: CreateUserResponseSchema
):
    """
    Проверяет, что ответ на создание пользователя соответствует запросу.

    :param request: Исходный запрос на создание пользователя.
    :param response: Ответ API с данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(response.user.email, request.email, "email")
    assert_equal(response.user.last_name, request.last_name, "last_name")
    assert_equal(response.user.first_name, request.first_name, "first_name")
    assert_equal(response.user.middle_name, request.middle_name, "middle_name")


def assert_user(actual: UserSchema, expected: UserSchema):
    """
    Проверяет, что информации о пользователе соответствует ожидаемой.

    :param actual: Проверяемая информация о пользователе.
    :param expected: Ожидаемая информация о пользователе.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.email, expected.email, "email")
    assert_equal(actual.last_name, expected.last_name, "last_name")
    assert_equal(actual.first_name, expected.first_name, "first_name")
    assert_equal(actual.middle_name, actual.middle_name, "middle_name")


def assert_get_user_response(
        get_user_response: GetUserResponseSchema,
        create_user_response: CreateUserResponseSchema
):
    """
    Проверяет, что ответ на создание пользователя соответствует запросу.

    :param get_user_response: Запрос на получение информации о пользователе.
    :param create_user_response: Ответ API с данными о создании пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    actual = get_user_response.user
    expected = create_user_response.user
    assert_user(actual, expected)
