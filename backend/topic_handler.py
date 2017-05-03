from google.appengine.ext import ndb

from backend_helper import BackendHelper

from proto.topic_proto import TopicProto
from model.topic_model import TopicModel
from model.topic_model import TopicResponseModel

import random
import logging

class TopicQuery:

    @staticmethod
    def get_topic_responses(topic_request):
        return ndb.gql(('SELECT * FROM TopicResponseModel '
                          'WHERE topic = :1'), topic_request.topic)

    @staticmethod
    def get_topic_response(topic_response):
        logging.info(topic_response)
        return ndb.Key('TopicResponseModel', topic_response.response).get()

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
        query = TopicModel.query()
        query = query.filter(TopicModel.topic >= query_str)

        results = query.fetch(10)
        return BackendHelper.topic_results_to_proto(results)

class TopicHandler:

    @staticmethod
    def handle_insert_topic(topic_request):
        TopicModel(rand_num=BackendHelper.generate_random_number(),
                    topic=topic_request.topic, id=topic_request.topic).put()

    @staticmethod
    def handle_insert_topic_response(topic_response):
        response_model = TopicQuery.get_topic_response(topic_response)
        if response_model is None:
            TopicResponseModel(id=topic_response.response,
                                topic=topic_response.topic,
                                response=topic_response.response,
                                count=0).put()
        else:
            response_model.count += 1
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
