from google.appengine.ext import endpoints
from google.appengine.ext import ndb

from topic_handler import TopicHandler

from proto.topic_proto import TopicRequestProto
from proto.topic_proto import TopicResponseProto
from proto.topic_proto import TopicStatus
from protorpc import remote


@endpoints.api(name='topic_api', version='v1', description='API for topics')
class TopicAPI(remote.Service):

    @endpoints.method(TopicRequestProto, TopicStatus,
        name='insert_topic', path='topic.insert_topic', http_method='POST')
    def insert_topic(self, request):
        TopicHandler.handle_insert_topic(request)
        return TopicStatus(status='OK')

    @endpoints.method(TopicRequestProto, TopicResponseProto,
        name='get_topic_responses', path='topic.get_topic_responses',
        http_method='GET')
    def get_topic_responses(self, request):
        results = TopicHandler.handle_get_topic_responses(request)
        print results
        return TopicResponseProto()

endpoints_application = endpoints.api_server([TopicAPI])
