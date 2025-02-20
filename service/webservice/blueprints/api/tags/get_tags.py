from flask.views import MethodView

from webservice import db, logger

from webservice.utils import HTTPResponse
from webservice.utils.decorators import cache_it

from spiderlib.db.db_modules.tag import Tag
from spiderlib.db import DBEncoderDict


class GetTagsApi(MethodView):

    """ /api/{api_version}/tags/<id> """

    # TODO: to implement: get a certain number of tags
    @cache_it(default_key='all_tags', entity_name='Tag', timeout=60)
    def get(self, number=None):

        """
        Returns tags data
            Args:
                number: the number of tags to show
            Return:
                Json obj
        """

        logger.info("get request, tags endpoint")

        try:
            tags = DBEncoderDict.list_to_dict(db.query(Tag))
            # redis.set('all_tags', tags)
            return HTTPResponse.accepted(data=tags)

        except Exception as error:
            logger.error(
                f"Something went wrong during requesting tags' data. Error: {error}"
            )
            return HTTPResponse.internal_server_error(
                message="Something went wrong during requesting tags' data"
            )
