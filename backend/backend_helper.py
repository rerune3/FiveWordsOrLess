from proto.topic_proto import TopicRequestProto
from proto.topic_proto import TopicResponseProto
from proto.topic_proto import TopicResponseListProto


class BackendHelper:

    @staticmethod
    def topic_response_results_to_proto(topic, response_results):
        response_list_proto = TopicResponseListProto(topic=topic)
        if response_results is None:
            return response_list_proto

        for response_model in response_results:
            proto = TopicResponseProto(topic=response_model.topic,
                                        response=response_model.response,
                                        count=response_model.count)
            response_list_proto.response_list.append(proto)

        return response_list_proto
