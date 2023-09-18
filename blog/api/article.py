import requests
from combojsonapi.event.resource import EventsResource
from flask import request
from flask_combo_jsonapi import ResourceDetail, ResourceList
from blog.schemas import ArticleSchema
from blog.extensions import db
from blog.models import Article



class ArticleListEvent(EventsResource):
    def event_get_count(self, *args, **kwargs):

        """
        The event_get_count function returns the number of articles in the database.

        :param self: Pass the instance of the class to a function
        :param *args: Send a non-keyworded variable length argument list to the function
        :param **kwargs: Pass a variable number of keyword arguments to a function
        :return: The number of articles in the database
        :doc-author: Trelent
        """
        return{'count': Article.query.count()}

    def event_post_count(self):
        """
        The event_post_count function is a GET request that returns the number of posts for each event.
            The function takes in an event_id and returns the count of posts associated with that id.

        :param self: Refer to the current instance of a class
        :return: A dictionary with the key 'method' and the value of
        :doc-author: Trelent
        """
        return{'method': request.method}

    def event_get_api_server(self):
        return {'count': requests.get('https://ifconfig.io/ip').text}


class ArticleDetailEvent(EventsResource):
    def event_get_count_by_author(self, *args, **kwargs):

        """
        The event_get_count_by_author function is a custom event that returns the number of articles written by an author.
        It takes in an id as a parameter and returns the count of articles with that author_id.

        :param self: Represent the instance of the class
        :param *args: Send a non-keyworded variable length argument list to the function
        :param **kwargs: Pass a variable number of keyword arguments to the function
        :return: The number of articles written by a specific author
        :doc-author: Trelent
        """
        return{'count': Article.query.filter(Article.author_id == kwargs['id']).count()}


class ArticleList(ResourceList):
    events = ArticleListEvent
    schema = ArticleSchema
    data_layer = {
        "session": db.session,
        "model": Article,
    }


class ArticleDetail(ResourceDetail):
    events = ArticleDetailEvent
    schema = ArticleSchema
    data_layer = {
        "session": db.session,
        "model": Article,
    }

