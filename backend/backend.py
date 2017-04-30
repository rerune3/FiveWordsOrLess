from google.appengine.ext import endpoints
from google.appengine.ext import ndb

from topic_handler import TopicHandler
from backend_helper import BackendHelper
from topics import TopicListString

from proto.topic_proto import TopicProto
from proto.topic_proto import TopicListProto
from proto.topic_proto import TopicResponseProto
from proto.topic_proto import TopicResponseListProto
from proto.topic_proto import TopicStatus

from protorpc import remote
from protorpc import message_types

import logging

@endpoints.api(name='topic_api', version='v1', description='API for topics')
class TopicAPI(remote.Service):

    @endpoints.method(TopicProto, TopicStatus,
        name='insert_topic', path='topic.insert_topic', http_method='POST')
    def insert_topic(self, request):
        TopicHandler.handle_insert_topic(request)
        return TopicStatus(status='OK')

    @endpoints.method(message_types.VoidMessage, message_types.VoidMessage,
        name='insert_topics_in_text_file',
            path='topic.insert_topics_in_text_file', http_method='POST')
    def insert_topics_in_text_file(self, request):
        str_list = TopicListString.__doc__.split('\n')
        for line in str_list:
            line = line.strip()
            topic_proto = TopicProto(topic=line)
            TopicHandler.handle_insert_topic(topic_proto)

        return message_types.VoidMessage()

    @endpoints.method(TopicResponseProto, TopicStatus,
        name='insert_topic_response', path='topic.insert_topic_response',
        http_method='POST')
    def insert_topic_response(self, topic_response):
        TopicHandler.handle_insert_topic_response(topic_response)
        return TopicStatus(status='OK')

    @endpoints.method(message_types.VoidMessage, TopicListProto,
        name='get_random_topic', path='topic.get_random_topic',
        http_method='GET')
    def get_random_topic(self, request):
        return TopicHandler.handle_get_random_topic()

    @endpoints.method(TopicProto, TopicResponseListProto,
        name='get_topic_responses', path='topic.get_topic_responses',
        http_method='GET')
    def get_topic_responses(self, request):
        results = TopicHandler.handle_get_topic_responses(request)
        return BackendHelper.topic_response_results_to_proto(request.topic, results)

endpoints_application = endpoints.api_server([TopicAPI])
