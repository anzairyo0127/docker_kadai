import os
from redis import Redis
host = os.getenv('REDIS_ADDRESS')
port = os.getenv('REDIS_PORT')
redis_cli = Redis(
    host=host,
    port=port,
)
redis_cli.set('test', 'This is Test Message!')
