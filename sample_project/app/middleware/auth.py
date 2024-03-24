from starlette.middleware.base import BaseHTTPMiddleware
from jose import JWTError, jwt
from fastapi.responses import JSONResponse
from app.common.common import get_public_key
from app.common.error_msg import ERROR_MSG
import os


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
                    {"error": {"code": 401, "message": ERROR_MSG.INVALID_TOKEN.value}}
                )

            request.state.decoded_token = payload
        response = await call_next(request)

        return response
