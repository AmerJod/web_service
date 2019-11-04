
from flask.views import MethodView
from sqlalchemy.orm.exc import NoResultFound

from webservice import db, logger
from webservice.utils import HTTPResponse
from webservice.utils.decorators import cache_it

from spiderlib.db.db_modules import Author
from spiderlib.db import DBEncoderDict


class GetAuthersApi(MethodView):
    """ /api/{api_version}/authors/<author_name> """


    @cache_it(default_key='all_authors', entity_name='Author', timeout=60)
    def get(self, author_name=None):

        """
        Returns Authors/Author data
            Args:
                author_name: the author name
            Return:
                json obj
        """

        logger.info("get request, authors endpoint")

        try:
            if author_name:
                exist, author = db.exist(Author, author_name=author_name)
                if exist:
                    # Return only one author's data
                    authors = DBEncoderDict().encode(author)
                    logger.debug(
                        f"Author's data: {author_name!r} has been retrieved - Authors get request"
                    )
                else:
                    # Wrong author name or not found in our db
                    raise NoResultFound
            else:
                # Get all the authors, need to iterate through all of them.
                authors = DBEncoderDict().list_to_dict(db.query(Author))
                logger.debug(f"All authors' data has been retrieved")

            return HTTPResponse.accepted(data=authors)

        except NoResultFound as error:
            logger.debug(f"Author's data: {author_name!r} has not been found")
            return HTTPResponse.not_found(
                message="This author's name has not been found in our Database"
            )

        except Exception as error:
            logger.error(
                f"Something went wrong during requesting authors' data. Error: {error}"
            )
            return HTTPResponse.internal_server_error(
                message="Something went wrong during requesting authors' data"
            )
