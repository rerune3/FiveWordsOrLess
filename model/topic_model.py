from google.appengine.ext import ndb

class TopicModel(ndb.Model):
    topic = ndb.StringProperty(required=True)
    rand_num = ndb.FloatProperty(required=True)

class TopicResponseModel(ndb.Model):
    topic = ndb.StringProperty(required=True)
    response = ndb.StringProperty(required=True)
    likes = ndb.IntegerProperty(required=False)
    dislikes = ndb.IntegerProperty(required=False)
