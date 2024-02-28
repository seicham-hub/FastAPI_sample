FROM python:3.11.7-slim-bookworm

RUN apt-get update && apt-get install -y git procps curl dnsutils \
    && pip install fastapi ariadne sqlalchemy aio-pika\
    && pip install "uvicorn[standard]" websocket broadcaster[redis] httpx \
    && pip install pyflakes black pytest pytest-mock pytest-asyncio pytest-cov


ENTRYPOINT ["bin/bash"]