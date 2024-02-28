from broadcaster import Broadcast
import os


pubsub = Broadcast(f"redis://{os.environ['REDIS_HOST']}:6379")
