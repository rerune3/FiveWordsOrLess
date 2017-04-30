import os
import json
import jinja2
import webapp2
import logging

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class HomePage(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('home.html')
        self.response.write(template.render(template_values))

    def post(self):
        logging.info(self.request.query_string)
        request_type = self.request.get('request_type')
        logging.info('hello')
        if request_type == 'INSERT_TOPIC_RESPONSE':
            pass
            data = json.loads(self.request.get('data'))
            response = RequestHandler.handle_insert_topic_response(data)
            self.response.write('Got it.')
        elif request_type == 'GET_TOPIC_RESPONSES':
            pass
            # comment = json.loads(self.request.get('comment'))
            # response = RequestHandler.handle_insert_new_comment(comment)
            # self.response.write(response)
        elif request_type == 'GET_RANDOM_TOPIC':
            pass
            # response = RequestHandler.handle_insert_new_comment()
            # self.response.write(response)
        elif request_type == 'GET_TOPIC':
            pass
            # response = RequestHandler.handle_insert_new_comment()
            # self.response.write(response)
        else:
            print 'Unknown request type %s' % (request)

        return

application = webapp2.WSGIApplication(
    [('/', HomePage)],
    debug=True)
