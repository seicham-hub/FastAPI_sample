from ariadne import (
    load_schema_from_path,
    make_executable_schema,
    ObjectType,
    SubscriptionType,
)

from app import controllers
from app.pub_sub_store import pubsub
import json

query = ObjectType("Query")
mutation = ObjectType("Mutation")
subscription = SubscriptionType()


@query.field("getUserById")
def resolve_get_user_by_id(_, info, input):
    return controllers.get_user_by_id(info, input)


@query.field("getAllUser")
def resolve_get_all_user(_, info):
    return controllers.get_all_user(info)


@mutation.field("createConversation")
def resolve_createConversation(_, info, input):
    return controllers.create_conversation(info, input)


@mutation.field("updateUserById")
def resolve_update_user_by_id(_, info, input):
    return {"result": True}


@mutation.field("sendMessage")
def resolve_send_message(_, info, input):
    return controllers.send_message(info, input)


@subscription.source("onNewConversationMessage")
async def message_generator(obj, info, input):
    async with pubsub.subscribe(channel="message_channel") as subscriber:
        async for row_message in subscriber:
            try:
                message = json.loads(row_message.message)

                if (message["conversation_id"]) == input["conversation_id"]:
                    yield message
            except Exception as e:
                print(e)


@subscription.field("onNewConversationMessage")
def resolve_on_new_conversation_message(message, info, input):
    return {"message": message.get("content", "")}


raw_schema = load_schema_from_path("/var/www/sample_project/app/schemas/schema.graphql")

schema = make_executable_schema(
    raw_schema,
    query,
    mutation,
    subscription,
    convert_names_case=True,
)
