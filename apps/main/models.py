from __future__ import unicode_literals
from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class SubscriberManager(models.Manager):
	def validate(self, post):
		isValid = True
		if not EMAIL_REGEX.match(post.get('email')):
			isValid = False
			print "1"
		if len(post.get('email')) == 0:
			isValid = False
			print "2"
		return isValid


class Subscriber(models.Model):
	email = models.EmailField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = SubscriberManager()
