from aio_pika import connect_robust
import os
import asyncio


async def _process_message(message):
    async with message.process():
        print("recieved message from rabbitMQ!", message)
        await asyncio.sleep(3)


async def start_rabbit_mq_reciever(loop, queue_name):
    connection = await connect_robust(
        f"amqp://guest:guest@{os.environ['RABBIT_MQ_HOST']}/",
        loop=loop,
    )

    # create channel
    channel = await connection.channel()

    # handle one task at a time
    await channel.set_qos(prefetch_count=1)

    # if you create queue on sending application,only one queue is created.
    # durable=True rabbitmq will never lose this queue
    queue = await channel.declare_queue(queue_name, durable=True)

    await queue.consume(_process_message)

    print(" [*] RabbitMQ reciever started! Waiting for messages.")
