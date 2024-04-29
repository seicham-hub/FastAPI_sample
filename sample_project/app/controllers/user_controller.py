from app import models
from sqlalchemy.exc import SQLAlchemyError
from app.common.error_msg import ERROR_MSG
from app.common.common import verify_password, create_access_token
from datetime import timedelta
import os


def login(info, input):
    try:
        password = input["password"]
        email = input["email"]
    except KeyError as e:
        print(e)
        return {
            "user_errors": [{"code": 400, "message": ERROR_MSG.INVALID_PARAMETER.value}]
        }

    try:
        user = models.get_user_by_email(email)
    except SQLAlchemyError as e:
        print(e)
        return {
            "user_errors": [{"code": 500, "message": ERROR_MSG.FAILED_TO_LOGIN.value}]
        }

    if not verify_password(password, user.password_hash):
        return {
            "user_errors": [{"code": 500, "message": ERROR_MSG.FAILED_TO_LOGIN.value}]
        }

    access_token_expires = timedelta(
        minutes=int(os.environ["ACCESS_TOKEN_EXPIRE_MINUTES"])
    )
    access_token = create_access_token(
        data={"user_id": user.id, "email": user.email},
        expires_delta=access_token_expires,
    )

    return {"access_token": access_token}


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
