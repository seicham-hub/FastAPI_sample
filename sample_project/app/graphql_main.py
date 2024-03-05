from fastapi import FastAPI
from ariadne.asgi import GraphQL
from fastapi.middleware.cors import CORSMiddleware
from app.resolver.resolver import schema


graphql_app = GraphQL(schema, debug=True)

api = FastAPI()

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
)


api.add_route("/", graphql_app)
api.add_websocket_route("/", graphql_app)
