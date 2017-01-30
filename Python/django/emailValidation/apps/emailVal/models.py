from __future__ import unicode_literals
from django.db import models
import re

# Create your models here.
class EmailManager(models.Manager):
	def validate(self, postData):
		email_regex = re.compile(r'^[a-xA-Z0-9.+_-]+@[a-xA-Z0-9.+_-]+\.[a-zA-Z]+$')
		return email_regex.match(postData)

	def register(self, postData):
		if self.validate(postData['address']):
			Email.emailManager.create(address=postData['address'])
			print ("^**^^**^ Prnting Email.objects.all()")
			print (Email.emailManager.all())
			print ('**** Register told me everything worked right ****')
			return True
		else:

			print ('**** Register said FAILURE TO REGISTER ****')
			return False

class Email(models.Model):
	address = models.EmailField()
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)
	emailManager = EmailManager()
