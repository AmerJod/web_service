import functools
from webservice.utils.redis.cache import get_cache, set_cache


def cache_it(default_key=None, entity_name=None, timeout=60):
    """
    Caching decorator
    deals only only with one key
     Args:
        default_key: key name
        entity_name: the class name
        timeout (int): timeout for cached data
     Return:
        data
    """
    def cache(func):
        @functools.wraps(func)
        def wrapper_debug(*args, **kwargs):
            key_name = default_key

            list_keys = [v for k, v in kwargs.items()]
            if len(list_keys) > 0:
                # Get only the first key
                key_name = list_keys[0]

            if key_name:
                data = get_cache(key_name=key_name, entity_name=entity_name)
                if data:
                    # Get data from caching server
                    return data

            # Get data from db
            data = func(*args, **kwargs)

            if data:
                # Cache the data before return it
                set_cache(key_name=key_name,data=data, entity_name=entity_name,timeout=timeout)
                # logger.debug(f"{func.__ca!r} returned {value!r}")

            return data
        return wrapper_debug
    return cache

