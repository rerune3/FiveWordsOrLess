from protorpc import messages

class TopicRequestProto(messages.Message):
    topic = messages.StringField(1, required=True)

class TopicResponseProto(messages.Message):
    response = messages.StringField(1, required=True)
    topic = messages.StringField(2, required=False)
    count = messages.IntegerField(3, required=False)

class TopicResponseListProto(messages.Message):
    topic = messages.StringField(1, required=True)
    response_list = messages.MessageField(TopicResponseProto, 2, repeated=True)

class TopicStatus(messages.Message):
    status = messages.StringField(1, required=True)
