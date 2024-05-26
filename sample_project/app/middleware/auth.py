from starlette.middleware.base import BaseHTTPMiddleware
from jose import JWTError, jwt
from fastapi.responses import JSONResponse
from app.common.common import get_public_key
from app.common.error_msg import ERROR_MSG
import os
from ariadne.asgi import WebSocketConnectionError


class AuthMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, request, call_next):

        if "no-auth" not in str(request.url):
            token = request.headers.get("Authorization")

            public_key = get_public_key()

            try:
                payload = jwt.decode(
                    token, public_key, algorithms=os.environ["ALGORITHM"]
                )
            except Exception:
                return JSONResponse(
                    {
                        "errors": [
                            {
                                "message": ERROR_MSG.INVALID_TOKEN.value,
                                "extensions": {"code": 401},
                            }
                        ]
                    }
                )

            request.state.decoded_token = payload
        response = await call_next(request)

        return response


class WebSocketAuth:
    def on_connect(self, websocket, params):
        # if not isinstance(params, dict):
        #     websocket.scope["connection_params"] = {}

        # token = params.get("token")
        # public_key = get_public_key()

        # try:
        #     payload = jwt.decode(token, public_key, algorithms=os.environ["ALGORITHM"])
        # except Exception:
        #     raise WebSocketConnectionError(
        #         {"error": {"code": 4403, "message": ERROR_MSG.INVALID_TOKEN.value}}
        #     )

        # # websocket.scope is a dict acting as a "bag"
        # # stores data for the duration of connection
        # websocket.scope["decoded_token"] = payload

        print("websocketハンドシェイク完了")

    def context_value(self, request, data):
        context = {}
        context["request"] = request

        # if request.scope["type"] == "websocket":
        #     # request is an instance of WebSocket
        #     # context.update(request.scope["connection_params"])
        #     context["decoded_token"] = request.scope["connection_params"]
        # # else:
        # #     context["token"] = request.META.get("authorization")
        return context
