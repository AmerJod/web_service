from flask import Flask


# ---------------- Flask Config
# get the config file
from webservice.utils import config
app = Flask(__name__)
app.config.from_object(config)


# ---------------- LOGGER
# Initialize logger for the web-service module
from spiderlib.logging import NewLogger
logger = NewLogger(logger_name='web-service', store_flag=True).get_logger()


# --------------- REDIS
# Establish the rides connection
import redis
redis = redis.Redis(**config.REDIS_CONN)
# Time to live - redis server
ttl = 31104000 # one year


# ---------------- DATABASE
# Establish the DB connection
from spiderlib.db.database import Database
db = Database(**config.POSTGRES_CONN)


# ---------------- WEB SERVICE
from webservice.blueprints.api import api
# Blueprints can be disabled by commenting them out below
app.register_blueprint(api)
# app.register_blueprint(views)


