from flask.views import MethodView

from webservice.utils import HTTPResponse
from webservice import logger


class HealthCheckApi(MethodView):
    def get(self):
        logger.debug("Health check Api has been called.")
        return HTTPResponse.ok(message="API is up running :)")
