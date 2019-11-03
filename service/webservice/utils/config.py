import os


class Config(object):
    # shard configurations will be here
    pass


class ProductionConfig(Config):
    REDIS_CONN = {"host": "redis", "port": 6379}

    POSTGRES_CONN = {
        "POSTGRES_URL": "0.0.0.0:54320",
        "POSTGRES_USER": "postgres",
        "POSTGRES_PW": "pwd123456",
        "POSTGRES_DB": "db_postgres",
    }

    # Enable and disable lazy_load
    DATABASE_LAZY_LOAD = False


class DevelopmentConfig(Config):
    REDIS_CONN = {"host": "redis", "port": 6379}

    POSTGRES_CONN = {
        "POSTGRES_URL": "0.0.0.0:54320",
        "POSTGRES_USER": "postgres",
        "POSTGRES_PW": "pwd123456",
        "POSTGRES_DB": "db_postgres",
    }

    # Enable and disable lazy_load
    DATABASE_LAZY_LOAD = False


def get_config(testing=False):
    flask_env = os.getenv("FLASK_ENV", "development")

    if not flask_env:
        print("No value set for FLASK_ENV, Production config loaded")
        return ProductionConfig()
    elif flask_env == "production":
        print("Production config loaded")
        return ProductionConfig()
    elif flask_env == "development":
        print("Development config loaded")
        return DevelopmentConfig()
    else:
        print("No value match for FLASK_ENV, Production config loaded")
        return ProductionConfig()
