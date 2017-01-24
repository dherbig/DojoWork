from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Email(models.Model):
	address = models.EmailField()
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)

class EmailManager(models.Manager):

	def validate(self, postData):
		EMAIL_REGEX = re.compile(r'^[a-xA-Z0-9.+_-]+@[a-xA-Z0-9.+_-]+\.[a-zA-Z]+$')
		return (EMAIL_REGEX.match(request.POST['address']))

	def register(self, postData):
		if self.validate():
			Email.objects.create(address=address)
		return true
