import os
import json
import jinja2
import webapp2
import logging

from middle_layer.request_handler import RequestHandler

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class HomePage(webapp2.RequestHandler):
    def get(self):
        request_type = self.request.get('request_type', None)
        if request_type:
            if request_type == 'GET_TOPIC_RESPONSES':
                data = json.loads(self.request.get('data'))
                response = RequestHandler.handle_get_topic_responses(data)
                self.response.write(response)
            elif request_type == 'GET_RANDOM_TOPIC':
                response = RequestHandler.handle_get_random_topic()
                self.response.write(response)
            elif request_type == 'GET_SEARCH_RESULTS':
                data = json.loads(self.request.get('data'))
                response = RequestHandler.handle_search_topics(data)
                self.response.write(response)
            else:
                print 'Unknown request type %s' % (request)
        else:
            template_values = {}
            template = JINJA_ENVIRONMENT.get_template('home.html')
            self.response.write(template.render(template_values))

        return

    def post(self):
        request_type = self.request.get('request_type', None)
        if request_type:
            if request_type == 'INSERT_TOPIC_RESPONSE':
                data = json.loads(self.request.get('data'))
                response = RequestHandler.handle_insert_topic_response(data)
                self.response.write(response)
            elif request_type == 'LIKE_TOPIC_RESPONSE':
                data = json.loads(self.request.get('data'))
                response = RequestHandler.handle_like_topic_response(data)
                self.response.write(response)
            elif request_type == 'DISLIKE_TOPIC_RESPONSE':
                data = json.loads(self.request.get('data'))
                response = RequestHandler.handle_dislike_topic_response(data)
                self.response.write(response)
            else:
                print 'Unknown request type %s' % (request)

        return

application = webapp2.WSGIApplication(
    [('/', HomePage)],
    debug=True)
