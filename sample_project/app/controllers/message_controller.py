from app import models
from sqlalchemy.exc import SQLAlchemyError
from app.common.error_msg import ERROR_MSG
from app.common.common import check_permission_for_conversation

import json

from app.pub_sub_store import pubsub


async def send_message(info, input):

    try:
        message = input["message"]
        conversation_id = input["conversation_id"]

        request = info.context["request"]
        decoded_token = request.state.decoded_token
        user_id = decoded_token.get("user_id")
    except KeyError as e:
        print(e)
        return {
            "user_errors": [{"code": 400, "message": ERROR_MSG.INVALID_PARAMETER.value}]
        }

    # この会話にメッセージを操作する権限があるかチェック
    if not check_permission_for_conversation(user_id, conversation_id):
        return {
            "user_errors": [{"code": 403, "message": ERROR_MSG.PERMISSION_DENIED.value}]
        }

    message_data_to_insert = {
        "user_id": user_id,
        "conversation_id": conversation_id,
        "message": message,
    }

    # メッセージを作成する
    try:
        models.create_message(message_data_to_insert)
    except SQLAlchemyError as e:
        print(e)
        return {
            "user_errors": [
                {"code": 500, "message": ERROR_MSG.FAILED_TO_CREATE_DATA.value}
            ]
        }

    message_to_publish = {
        "conversation_id": conversation_id,
        "sender": user_id,
        "content": message,
    }
    await pubsub.publish("message_channel", json.dumps(message_to_publish))

    return {"result": True}
