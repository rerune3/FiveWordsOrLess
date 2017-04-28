from protorpc import messages

class TopicRequestProto(messages.Message):
    topic = messages.StringField(1, required=True)

class TopicResponseProto(messages.Message):
    topic_response = messages.StringField(1, required=True)
    count = messages.IntegerField(2, required=False)

class TopicStatus(messages.Message):
    status = messages.StringField(1, required=False)
