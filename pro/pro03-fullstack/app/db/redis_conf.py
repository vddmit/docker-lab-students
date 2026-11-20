import os
import redis

from dotenv import load_dotenv

load_dotenv

pool = redis.ConnectionPool(
    host=os.getenv("REDIS_HOST"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    username=os.getenv("REDIS_USER"),
    password=os.getenv("REDIS_USER_PASSWORD"),
    max_connections=10,
    decode_responses=True,
)

client = redis.Redis(connection_pool=pool)
