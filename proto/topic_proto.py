from protorpc import messages

class TopicProto(messages.Message):
    topic = messages.StringField(1, required=True)
    rand_num = messages.FloatField(2, required=False)

class TopicListProto(messages.Message):
    topic_list = messages.MessageField(TopicProto, 1, repeated=True)

class TopicResponseProto(messages.Message):
    response = messages.StringField(1, required=True)
    topic = messages.StringField(2, required=False)
    count = messages.IntegerField(3, required=False)

class TopicResponseListProto(messages.Message):
    topic = messages.StringField(1, required=True)
    response_list = messages.MessageField(TopicResponseProto, 2, repeated=True)

class TopicStatus(messages.Message):
    status = messages.StringField(1, required=True)
