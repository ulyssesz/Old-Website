from google.appengine.ext import webapp
from google.appengine.api import mail
from google.appengine.api import users

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import logging
import wsgiref.handlers

class InviteFriendHandler(webapp.RequestHandler):
	def post(self):

		from_addr = self.request.get("email")

		message = mail.EmailMessage()
		message.sender = "me@ulysseszheng0.appspotmail.com"
		message.to = "ulysses147@gmail.com"
		message.body = "Sent from: %s.\nBody:\n%s" % (from_addr, self.request.get("message"))
		message.subject = "Message from: %s" % from_addr
		logging.info("sending to %s" % message.sender)
		message.send()
	def get(self):
		logging.info("sdfasfdasfas Hello get")
def main():
	application = webapp.WSGIApplication([('/.*', InviteFriendHandler),
										('/contact_me.py', InviteFriendHandler)], debug=True)
	run_wsgi_app(application)


if __name__ == '__main__':
	main()