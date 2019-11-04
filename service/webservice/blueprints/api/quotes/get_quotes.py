from flask.views import MethodView
from sqlalchemy.orm.exc import NoResultFound

from webservice import db, logger, cache
from webservice.utils import HTTPResponse
from webservice.utils.decorators import cache_it

from spiderlib.db.db_modules.author import Author
from spiderlib.db.db_modules.quote import Quote
from spiderlib.db import DBEncoderDict



class GetQuotesApi(MethodView):
    """ /api/{api_version}/quotes/<author_name> """

    @cache_it(default_key='all_quotes', entity_name='Quotes', timeout=60)
    def get(self, author_name=None):

        """
        Returns quotes data
            Args:
                author_name: the author name
            Return:
                json obj
        """

        logger.info("get request, quotes endpoint")

        try:
            if author_name:
                # Get data for a specific author
                exist, author = db.exist(Author, author_name=author_name)
                logger.debug(
                    f"Author's data: {author_name!r} has been retrieved - Quotes get request"
                )
                if exist:
                    # Query only the quotes for a specific author
                    obj = db.query(Quote, author_id=author.author_id)
                    quotes = DBEncoderDict.list_to_dict(obj)

                else:
                    raise NoResultFound
            else:
                # Get all the author form DB
                quotes = DBEncoderDict.list_to_dict(db.query(Quote))
                logger.debug(f"All Quotes' data has been retrieved")

            return HTTPResponse.accepted(data=quotes)

        except NoResultFound as error:
            logger.debug(f"Author's data: {author_name!r} has not been found")
            return HTTPResponse.not_found(
                message="This author's name has not been found in our Database"
            )

        except Exception as error:
            logger.error(
                f"Something went wrong during requesting quotes' data. Error: {error}"
            )
            return HTTPResponse.internal_server_error(
                message="Something went wrong during requesting quotes' data"
            )
