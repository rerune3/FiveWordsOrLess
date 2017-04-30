import json
import urllib
import urllib2
import logging

from google.appengine.api import urlfetch

TOPICS_API_URL = 'http://localhost:8080/_ah/api/topic_api/v1'

class RequestHandler:

    @staticmethod
    def send_post_request(url, data):
        data = urllib.urlencode(data)
        result = urlfetch.fetch(url=url + data, method=urlfetch.POST)
        return result.content

    @staticmethod
    def send_get_request(url, data):
        data = urllib.urlencode(data)
        result = urlfetch.fetch(url=url + data, method=urlfetch.GET)
        return result.content

    @staticmethod
    def handle_insert_topic_response(data):
        url = '%s/topic.insert_topic_response?' % (TOPICS_API_URL);
        return RequestHandler.send_post_request(url, data)

    @staticmethod
    def handle_get_random_topic():
        url = '%s/topic.get_random_topic?' % (TOPICS_API_URL);
        return RequestHandler.send_get_request(url, {})

    @staticmethod
    def handle_get_topic_responses(data):
        url = '%s/topic.get_topic_responses?' % (TOPICS_API_URL);
        return RequestHandler.send_get_request(url, data)
