from fastapi import FastAPI
from ariadne.asgi import GraphQL

from app.resolver.resolver import schema


graphql_app = GraphQL(schema, debug=True)

api = FastAPI()


api.add_route("/", graphql_app)
api.add_websocket_route("/", graphql_app)
