from flask import Blueprint
from .health_check import HealthCheckApi

from .authors.get_authors import GetAuthersApi
from .tags.get_tags import GetTagsApi
from .quotes.get_quotes import GetQuotesApi


# This file is used as a registry for API endpoints

api_version = "v1"
api = Blueprint("api", __name__, url_prefix=f"/api/{api_version}")

api.add_url_rule("/healthcheck", view_func=HealthCheckApi.as_view("api_health_check"))

# Tag APIs
api.add_url_rule("/tags", view_func=GetTagsApi.as_view("api_get_all_tags"))
api.add_url_rule(
    "/tags/limit/<number>", view_func=GetTagsApi.as_view("api_get_tags_data_number")
)

# Author APIs
api.add_url_rule("/authors", view_func=GetAuthersApi.as_view("api_get_authors_data"))
api.add_url_rule(
    "/authors/filter/<author_name>",
    view_func=GetAuthersApi.as_view("api_get_author_data"),
)

# Quote APIs
api.add_url_rule("/quotes", view_func=GetQuotesApi.as_view("api_get_quotes_data"))
api.add_url_rule(
    "/quotes/filter/<author_name>",
    view_func=GetQuotesApi.as_view("api_get_quotes_data_by_author"),
)

# api.add_url_rule("//<record_id>", view_func=GetResourceApi.as_view("api_get_resource_status"))
