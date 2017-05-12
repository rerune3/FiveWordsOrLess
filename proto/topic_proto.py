from protorpc import messages

class TopicProto(messages.Message):
    topic = messages.StringField(1, required=True)
    rand_num = messages.FloatField(2, required=False)

class TopicListProto(messages.Message):
    topic_list = messages.MessageField(TopicProto, 1, repeated=True)

class FootprintProto(messages.Message):
    ip_address = messages.StringField(1, required=True)

class TopicResponseProto(messages.Message):
    uuid = messages.StringField(1, required=False)
    response = messages.StringField(2, required=False)
    topic = messages.StringField(3, required=False)
    likes = messages.IntegerField(4, required=False)
    dislikes = messages.IntegerField(5, required=False)

class TopicResponseListProto(messages.Message):
    topic = messages.StringField(1, required=True)
    response_list = messages.MessageField(TopicResponseProto, 2, repeated=True)

class SearchProto(messages.Message):
    search_string = messages.StringField(1, required=True)

class TopicStatus(messages.Message):
    status = messages.StringField(1, required=True)
