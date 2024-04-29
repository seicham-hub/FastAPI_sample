from app import models
from sqlalchemy.exc import SQLAlchemyError
from app.common.error_msg import ERROR_MSG
from app.common.common import check_permission_for_conversation

from app.database.database import get_db_session


def create_conversation(info, input):
    try:
        group_user_ids: list = [] if input["user_ids"] is None else input["user_ids"]
        request = info.context["request"]
        decoded_token = request.state.decoded_token
        user_id: int = decoded_token.get("user_id")
        group_user_ids.append(user_id)
    except KeyError as e:
        print(e)
        return {
            "user_errors": [{"code": 400, "message": ERROR_MSG.INVALID_PARAMETER.value}]
        }

    try:

        with get_db_session() as session:
            conversation_id: int = models.create_conversation(session)

            conversation_user_relation_data_to_insert = [
                {
                    "conversation_id": conversation_id,
                    "user_id": user_id,
                }
                for user_id in group_user_ids
            ]
            models.create_conversation_user_relation(
                conversation_user_relation_data_to_insert,
                session,
            )
    except SQLAlchemyError as e:
        print(e)
        return {
            "user_errors": [
                {"code": 403, "message": ERROR_MSG.FAILED_TO_CREATE_DATA.value}
            ]
        }

    return {"result": True}
