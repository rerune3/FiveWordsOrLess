import os
import json
import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class HomePage(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template = JINJA_ENVIRONMENT.get_template('static/index.html')
        self.response.write(template.render(template_values))

    def post(self):
        pass

application = webapp2.WSGIApplication(
    [('/', HomePage)],
    debug=True)
