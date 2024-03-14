from app import models
from sqlalchemy.exc import SQLAlchemyError
from app.common.error_msg import ERROR_MSG
from common.common import verify_password


def authenticate_user(info, input):
    try:
        password = input["password"]
        email = input["email"]
    except KeyError as e:
        print(e)
    try:
        user = models.get_user_by_email(email)
    except SQLAlchemyError as e:
        print(e)

        return {
            "user_errors": [
                {"code": 500, "message": ERROR_MSG.FAILED_TO_RETRIEVE_DATA.value}
            ]
        }

    verify_password(password, user.password_hash)


def get_user_by_id(info, input):

    try:
        request = info.context["request"]
        decoded_token = request.state.decoded_token
        user_id = decoded_token.get("user_id")
    except KeyError as e:
        print(e)
        return {
            "user_errors": [{"code": 400, "message": ERROR_MSG.INVALID_PARAMETER.value}]
        }
    try:
        user = models.get_user_by_id(user_id)
    except SQLAlchemyError:
        return {
            "user_errors": [
                {"code": 500, "message": ERROR_MSG.FAILED_TO_RETRIEVE_DATA.value}
            ]
        }

    return {"result": user}


def get_all_user(info):
    try:
        users: list = models.get_all_user()
    except SQLAlchemyError as e:
        print(e)
        return {
            "user_errors": [
                {"code": 500, "message": ERROR_MSG.FAILED_TO_RETRIEVE_DATA.value}
            ]
        }

    return {"result": users}
