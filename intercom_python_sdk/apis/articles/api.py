""" 
====================
Articles API
====================
`apis/articles/api.py`

This module contains the ArticlesAPI class, which defines a client for the Articles API.
It is used to interact with the Intercom Articles API [1] as defined in the Intercom API Reference [2].

----
[1] https://developers.intercom.com/intercom-api-reference/reference/articles
[2] https://github.com/intercom/Intercom-OpenAPI
"""

# Built-ins
import functools
from typing import Union, cast

# External
from uplink import (
    get, put, post,
    returns, args,
    error_handler, response_handler,
    Field, Body, json, Url, Path, Query,delete
)

# From Current API
from .schemas import (
    ArticleSchema,
    ArticleStatisticsSchema,
    CreateArticleSchema,
    DeletedArticleSchema
)
from .models import Article, ArticleStatistics, CreateArticle

# From Current Package
from ...core.api_base import APIBase
from ...core.errors import catch_api_error

@response_handler(catch_api_error)
class ArticlesAPI(APIBase):
    URI = "/articles/"

    @returns(ArticleSchema(many=False)) # type: ignore
    @get("{article_id}")
    def get_by_id(self, article_id: Union[str, int]):
        """ Get an Article by ID.

        Args:
            article_id (Union[str, int]): The ID of the Article.

        Returns:
            Article: The Article with the given ID.
        """
    
    @returns(ArticleSchema(many=False)) # type: ignore
    @post("")
    def create(self, data: Body(type=CreateArticleSchema)): # type: ignore

        """ Create an Article.

        Args:
            data (Body(type=CreateArticleSchema)): The data to create the Article with.

        Returns:
            Article: The created Article.
        """


    @returns(DeletedArticleSchema(many=False)) # type: ignore
    @delete("{article_id}")
    def delete_by_id(self, article_id: Union[str, int]):
        """ Delete an Article by ID.

        Args:
            article_id (Union[str, int]): The ID of the Article.

        Returns:
            DeletedArticle: The deleted Article.
        """




