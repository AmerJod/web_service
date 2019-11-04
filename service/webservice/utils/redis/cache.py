
from webservice import cache
from webservice import logger

# Get the default timeout
timeout = cache.config.get("CACHE_DEFAULT_TIMEOUT")

def get_cache(key_name, entity_name=None):
    """
    Gets cached data from the caching server - redis
        Args:
         key_name (str): key name
        Return:
         data (str)
    """
    try:
        if key_name:
            data = cache.get(key_name)
            if data:
                print(key_name)
                logger.debug(f"{entity_name} - Data have been retrieved from cache, key: {key_name}")
                return data
            return None

    except Exception as error:
        logger.error(f"Problem with retrieving cached data - {entity_name}, Error: {error}")
        return None


def set_cache(key_name, data, entity_name=None, timeout=timeout):
    """
    Sets data into the caching server - redis
        Args:
         key_name (str): key name
         data (str): data
        Return:
             bool
    """
    try:
        if key_name:
            cache.set(key_name, data, timeout=timeout)
            logger.debug(f"{entity_name} - Data have been cached for {timeout}s , key: {key_name}")
            return True

    except Exception as error:
        logger.error(f"Problem with caching data - {entity_name}, Error: {error}")
        return False


