from google.appengine.ext import ndb

from proto.topic_proto import TopicRequestProto
from model.topic_model import TopicModel


class TopicQuery:

    @staticmethod
    def get_topic_responses(topic_request):
        return ndb.gql(('SELECT * FROM TopicResponseModel '
                          'WHERE topic = :1'), topic_request.topic)


class TopicHandler:

    @staticmethod
    def handle_insert_topic(topic_request):
        TopicModel(topic=topic_request.topic, id=topic_request.topic).put()

    @staticmethod
    def handle_get_topic_responses(topic_request):
        return ndb.Key('TopicResponseModel', topic_request.topic).get()
