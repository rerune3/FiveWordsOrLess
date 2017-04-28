from proto.topic_proto import TopicRequestProto
from model.topic_model import TopicModel


class TopicQuery:

    @staticmethod
    def get_topic_responses(topic_request):
        results = ndb.gql(('SELECT * FROM TopicResponseModel '
                          'WHERE PostID = :1'), list_request.post_id)


class TopicHandler:

    @staticmethod
    def handle_insert_topic(topic_request):
        TopicModel(topic=topic_request.topic, id=topic_request.topic).put()

    @staticmethod
    def handle_get_topic_responses(topic_request):
        TopicResponseModel
        TopicModel(topic=topic_request.topic, id=topic_request.topic).put()
