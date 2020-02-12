from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

import redis

pool = redis.ConnectionPool(host='localhost', port=6379, db=1, decode_responses=True)
redis_cli = redis.Redis(connection_pool=pool)
