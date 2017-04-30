from proto.topic_proto import TopicProto
from proto.topic_proto import TopicListProto
from proto.topic_proto import TopicResponseProto
from proto.topic_proto import TopicResponseListProto

import random

class BackendHelper:

    @staticmethod
    def topic_response_model_to_proto(topic_response_model):
        return TopicResponseProto(topic=topic_response_model.topic,
                                    response=topic_response_model.response,
                                    count=topic_response_model.count)

    @staticmethod
    def topic_model_to_proto(topic_model):
        return TopicProto(topic=topic_model.topic,
                            rand_num=topic_model.rand_num)

    @staticmethod
    def topic_response_results_to_proto(topic, response_results):
        response_list_proto = TopicResponseListProto(topic=topic)
        if response_results is None:
            return response_list_proto

        for response_model in response_results:
            proto = BackendHelper.topic_response_model_to_proto(response_model)
            response_list_proto.response_list.append(proto)

        return response_list_proto

    @staticmethod
    def topic_results_to_proto(topic_results):
        topic_list_proto = TopicListProto()
        if topic_results is None:
            return topic_list_proto

        for topic_model in topic_results:
            proto = BackendHelper.topic_model_to_proto(topic_model)
            topic_list_proto.topic_list.append(proto)

        return topic_list_proto

    @staticmethod
    def generate_random_number():
        return random.random()
