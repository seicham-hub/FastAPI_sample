from ariadne import (
    load_schema_from_path,
    make_executable_schema,
    ObjectType,
)

from app import controllers

query = ObjectType("Query")


@query.field("login")
def resolve_login(_, info, input):
    return controllers.login(info, input)


raw_schema = load_schema_from_path(
    "/var/www/sample_project/app/schemas/no_auth_schema.graphql"
)

schema = make_executable_schema(
    raw_schema,
    query,
    convert_names_case=True,
)
