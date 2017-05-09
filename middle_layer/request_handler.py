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
    def handle_like_topic_response(data):
        url = '%s/topic.like_topic_response?' % (TOPICS_API_URL);
        return RequestHandler.send_post_request(url, data)

    @staticmethod
    def handle_dislike_topic_response(data):
        url = '%s/topic.dislike_topic_response?' % (TOPICS_API_URL);
        return RequestHandler.send_post_request(url, data)

    @staticmethod
    def handle_get_random_topic():
        url = '%s/topic.get_random_topic?' % (TOPICS_API_URL);
        return RequestHandler.send_get_request(url, {})

    @staticmethod
    def handle_get_topic_responses(data):
        url = '%s/topic.get_topic_responses?' % (TOPICS_API_URL);
        responses = RequestHandler.send_get_request(url, data)
        responses_obj = json.loads(responses)
        response_list = responses_obj.get('response_list', None)

        if (response_list is None):
            return ''

        response_html = ''
        for response in response_list:
            html = '''
                  <div id='%s' class='topic_response'>
                    <div class='response_text_wrapper'>
                      <p class='response_text'>%s</p>
                    </div>
                    <div class='likedislike_button_wrapper'>
                      <div class='like_wrapper'>
                        <button class='like_button'>Like</button>
                        <p class='like_count'>%s</p>
                      </div>
                      <div class='dislike_wrapper'>
                        <button class='dislike_button'>Dislike</button>
                        <p class='dislike_count'>%s</p>
                      </div>
                    </div>
                  </div>
                  ''' % (response['uuid'], response['response'],
                        response['likes'], response['dislikes'])

            response_html = '%s\n%s' % (response_html, html)

        return response_html

    @staticmethod
    def handle_search_topics(data):
        url = '%s/topic.search_topics?' % (TOPICS_API_URL);
        results = RequestHandler.send_get_request(url, data)
        results_obj = json.loads(results)
        results_list = results_obj.get('topic_list', None)

        if (results_list is None):
            return ''

        response_html = ''
        for topic in results_list:
            html = '''
                <div class='search_result'>
                    <p class='search_result_text'>%s</p>
                </div>
                ''' % (topic['topic'])
            response_html = '%s\n%s' % (response_html, html)

        return response_html
