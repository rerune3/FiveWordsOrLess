from google.appengine.ext import ndb

class TopicModel(ndb.Model):
    topic = ndb.StringProperty(required=True)

class TopicResponseModel(ndb.Model):
    topic = ndb.StringProperty(required=True)
    topic_response = ndb.StringProperty(required=True)
    count = ndb.IntegerProperty(required=True)
