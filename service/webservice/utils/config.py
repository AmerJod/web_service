import os


class Config(object):
    # shard configurations will be here
    pass


class ProductionConfig(Config):
    """
        Configuration for production environment
    """

    POSTGRES_CONN = {
        "POSTGRES_URL": "postgres",
        "POSTGRES_USER": "postgres",
        "POSTGRES_PW": "postgres",
        "POSTGRES_DB": "postgres",
    }

    REDIS_CONFIG = {
        "CACHE_TYPE": "redis",
        "CACHE_KEY_PREFIX": "fcache",
        "CACHE_REDIS_HOST": "redis",
        "CACHE_REDIS_PORT": "6379",
        "CACHE_DEFAULT_TIMEOUT": 300,
        'CACHE_REDIS_URL': "redis://redis:6379"
    }

    # Enable and disable lazy loading the db
    DATABASE_LAZY_LOAD = False


class DevelopmentConfig(Config):
    """
        Configuration for development environment
    """


    POSTGRES_CONN = {
        "POSTGRES_URL": "0.0.0.0:54320",
        "POSTGRES_USER": "postgres",
        "POSTGRES_PW": "postgres",
        "POSTGRES_DB": "postgres",
    }

    REDIS_CONFIG = {
        "CACHE_TYPE": "redis",
        "CACHE_KEY_PREFIX": "fcache",
        "CACHE_REDIS_HOST": "redis",
        "CACHE_REDIS_PORT": "6379",
        "CACHE_DEFAULT_TIMEOUT": 300,
        'CACHE_REDIS_URL': "redis://redis:6379"
    }

    # Enable and disable lazy loading for the db
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
