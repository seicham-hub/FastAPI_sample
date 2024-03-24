from ariadne import (
    load_schema_from_path,
    make_executable_schema,
    ObjectType,
)

from app import controllers

query = ObjectType("Query")
mutation = ObjectType("Mutation")


@query.field("getUserById")
def resolve_get_user_by_id(_, info, input):
    return controllers.get_user_by_id(info, input)


@query.field("getAllUser")
def resolve_get_all_user(_, info):
    return controllers.get_all_user(info)


@mutation.field("updateUserById")
def resolve_update_user_by_id(_, info, input):
    return {"result": True}


raw_schema = load_schema_from_path("/var/www/sample_project/app/schemas/schema.graphql")

schema = make_executable_schema(
    raw_schema,
    query,
    mutation,
    convert_names_case=True,
)
