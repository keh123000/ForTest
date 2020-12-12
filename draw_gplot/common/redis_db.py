from redis import Redis, StrictRedis, ConnectionPool

from config import DevConfig

# url = 'redis://:123456@192.168.0.178:6379/0'
pool = ConnectionPool.from_url(DevConfig.REDIS_DATABASE_URI)
redis = StrictRedis(connection_pool=pool)
