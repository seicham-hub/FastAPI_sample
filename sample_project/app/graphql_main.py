from fastapi import FastAPI
from ariadne.asgi import GraphQL
from ariadne.asgi.handlers import GraphQLTransportWSHandler
from fastapi.middleware.cors import CORSMiddleware
from app.resolver.resolver import schema
from app.resolver.no_auth_resolver import schema as no_auth_schema
from app.middleware.auth import AuthMiddleware, WebSocketAuth


wsAuth = WebSocketAuth()

graphql_app = GraphQL(
    schema,
    context_value=wsAuth.context_value,
    websocket_handler=GraphQLTransportWSHandler(on_connect=wsAuth.on_connect),
    debug=True,
)
graphql_no_auth_app = GraphQL(no_auth_schema, debug=True)

api = FastAPI()

api.add_middleware(AuthMiddleware)
api.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost", "http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# ルート登録
api.add_route("/", graphql_app)
api.add_route("/no-auth", graphql_no_auth_app)
# websocketのルート
api.add_websocket_route("/", graphql_app)
