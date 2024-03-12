FROM python:3.11.7-slim-bookworm

COPY requirements.txt ./

RUN apt-get update && apt-get install -y git procps curl dnsutils \
    && pip install -r requirements.txt

ENTRYPOINT ["bin/bash"]