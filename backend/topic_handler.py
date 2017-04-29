from google.appengine.ext import ndb

from proto.topic_proto import TopicRequestProto
from model.topic_model import TopicModel
from model.topic_model import TopicResponseModel

class TopicQuery:

    @staticmethod
    def get_topic_responses(topic_request):
        return ndb.gql(('SELECT * FROM TopicResponseModel '
                          'WHERE topic = :1'), topic_request.topic)

    @staticmethod
    def get_topic_response(topic_response):
        return ndb.Key('TopicResponseModel', topic_response.response).get()

class TopicHandler:

    @staticmethod
    def handle_insert_topic(topic_request):
        TopicModel(topic=topic_request.topic, id=topic_request.topic).put()

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
        pass

    @staticmethod
    def handle_get_topic_responses(topic_request):
        return TopicQuery.get_topic_responses(topic_request)
