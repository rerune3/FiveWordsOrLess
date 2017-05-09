from google.appengine.ext import ndb

from backend_helper import BackendHelper

from proto.topic_proto import TopicProto
from model.topic_model import TopicModel
from model.topic_model import TopicResponseModel

import random
import logging
import uuid

class TopicQuery:

    @staticmethod
    def get_topic_responses(topic_request):
        return ndb.gql(('SELECT * FROM TopicResponseModel '
                          'WHERE topic = :1 ORDER BY likes DESC'),
                          topic_request.topic)

    @staticmethod
    def get_topic_response(topic_response):
        return ndb.Key('TopicResponseModel', topic_response.uuid).get()

    @staticmethod
    def get_random_topic():
        rand_num1 = BackendHelper.generate_random_number()
        rand_num2 = BackendHelper.generate_random_number()
        query = TopicModel.query()
        query = query.filter(TopicModel.rand_num >= min(rand_num1, rand_num2))
        query = query.filter(TopicModel.rand_num <= max(rand_num1, rand_num2))

        results = query.fetch(1)
        return BackendHelper.topic_results_to_proto(results)

    @staticmethod
    def get_search_matches(search_request):
        query_str = search_request.search_string
        query_str_variations = [query_str, query_str.title(), query_str.upper()]

        query = TopicModel.query()
        query = query.filter(ndb.OR(TopicModel.topic >= query_str_variations[0],
                                TopicModel.topic >= query_str_variations[1],
                                TopicModel.topic >= query_str_variations[2]))

        results = query.fetch(50)
        return BackendHelper.topic_results_to_proto(results)

class TopicHandler:

    @staticmethod
    def handle_insert_topic(topic_request):
        TopicModel(rand_num=BackendHelper.generate_random_number(),
                    topic=topic_request.topic, id=topic_request.topic).put()

    @staticmethod
    def handle_insert_topic_response(topic_response):
        TopicResponseModel(id=uuid.uuid4().hex,
                            topic=topic_response.topic,
                            response=topic_response.response,
                            likes=0, dislikes=0).put()

    @staticmethod
    def handle_like_topic_response(topic_response):
        response_model = TopicQuery.get_topic_response(topic_response)
        response_model.likes += 1
        response_model.put()

    @staticmethod
    def handle_dislike_topic_response(topic_response):
        response_model = TopicQuery.get_topic_response(topic_response)
        response_model.dislikes += 1
        response_model.put()

    @staticmethod
    def handle_get_random_topic():
        return TopicQuery.get_random_topic()

    @staticmethod
    def handle_get_topic_responses(topic_request):
        return TopicQuery.get_topic_responses(topic_request)

    @staticmethod
    def handle_search_topics(search_request):
        return TopicQuery.get_search_matches(search_request)
