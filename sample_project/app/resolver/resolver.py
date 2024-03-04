from ariadne import (
    load_schema_from_path,
    make_executable_schema,
    ObjectType,
)

query = ObjectType("Query")
mutation = ObjectType("Query")


@query.field("getAllUser")
def resolve_get_all_user(_, info, input):
    # request = info.context["request"]
    # user_agent = request.headers.get("user-agent", "guest")
    return {"result": {"id": 1, "name": "yamada taro"}}


@mutation.field("updateUserById")
def resolve_update_user_by_id(_, info, input):
    return {"result": True}


raw_schema = load_schema_from_path("/var/www/sample_project/app/schemas/schema.graphql")

schema = make_executable_schema(
    raw_schema,
    query,
    convert_names_case=True,
)
