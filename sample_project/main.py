from fastapi import FastAPI

# from app.rest_api_main import api as rest_api
from app.graphql_main import api as graphql_api
from app.pub_sub_store import pubsub
from app.modules import start_rabbit_mq_reciever
from contextlib import asynccontextmanager
import asyncio
import uvicorn
import os


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup時のイベント
    pubsub.connect

    loop = asyncio.get_running_loop()
    queue_name = "heavy_task_finished"
    loop.create_task(start_rabbit_mq_reciever(loop, queue_name))

    yield

    # shutdown時のイベント
    pubsub.disconnect()


app = FastAPI(lifespan=lifespan)
# app.mount("/rest", rest_api)
app.mount("/graphql", graphql_api)

if __name__ == "__main__":
    if os.environ["MODE"] == "local":
        uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
    else:
        uvicorn.run("main:app", host="0.0.0.0", port=8000, workers=4)
