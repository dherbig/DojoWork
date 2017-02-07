from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import validate_email, EmailValidator
import bcrypt, re, datetime
# Create your models here.

#Our validators:
def valGT2(value):
	if len(value)<3:
		raise ValidationError(
			'{} must be longer than 2'.format(value)
		)

def valGT8(value):
	if len(value)<8:
		raise ValidationError(
			'{} must be 8 or more characters'.format(value)
		)

# Object information
class User(models.Model):
	first_name = models.CharField(max_length=45, validators = [valGT2])
	last_name = models.CharField(max_length=45, validators = [valGT2])
	email = models.EmailField(max_length=254, validators = [validate_email])
	password = models.CharField(max_length=100, validators = [valGT8])
	dob = models.DateField(max_length=10)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
