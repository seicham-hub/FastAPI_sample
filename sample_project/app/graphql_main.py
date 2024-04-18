from fastapi import FastAPI
from ariadne.asgi import GraphQL
from ariadne.asgi.handlers import GraphQLTransportWSHandler
from fastapi.middleware.cors import CORSMiddleware
from app.resolver.resolver import schema
from app.resolver.no_auth_resolver import schema as no_auth_schema
from app.middleware.auth import AuthMiddleware


def on_connect(websocket, params):
    # if not isinstance(params, dict):
    #     websocket.scope["connection_params"] = {}

    # # websocket.scope is a dict acting as a "bag"
    # # stores data for the duration of connection
    # websocket.scope["connection_params"] = {
    #     "token": params.get("token"),
    # }
    print("websocketハンドシェイク完了")


graphql_app = GraphQL(
    schema,
    websocket_handler=GraphQLTransportWSHandler(on_connect=on_connect),
    debug=True,
)
graphql_no_auth_app = GraphQL(no_auth_schema, debug=True)

api = FastAPI()

api.add_middleware(AuthMiddleware)
api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
)


api.add_route("/", graphql_app)
api.add_route("/no-auth", graphql_no_auth_app)

api.add_websocket_route("/", graphql_app)
