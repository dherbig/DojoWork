from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
import bcrypt, re
# Create your models here.

class UserManager(models.Manager):
	def check_user(self, postData):
		errors = []
		print (self.filter(email=postData['email']))
		user = self.filter(email=postData['email'])[0]
		if user:
			#check Passwords
			if not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
				errors.append('Wrong password!')
			else:
				print user.id
				return {'user_id': user.id}
		else:
			errors.append(request, 'No such user!')
		return {'errors': errors}

	def register(self, postData):
		print ("Begining registration process:")
		print (postData)
		email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')
		#Tracks Errors:
		errors = []
		# 4 validations needed
		# First Name longer than 2 characters, letters only
		if not len(postData['first_name']) > 2:
			print(postData['first_name'])
			errors.append("Names must be at least 3 characters long!")
		# Last Name longer than 2 characters, letters only
		if not len(postData['last_name']) > 2:
			print(postData['last_name'])
			errors.append("Names must be at least 3 characters long!")
		# Email: required, valid format
		if not email_regex.match(postData['email']):
			print(postData['email'])
			errors.append("Not a valid email!")
		# password 8+ characters...
		if not len(postData['password'])>7:
			print(postData['password'])
			errors.append("Password is too short!")
		# ...matches teh confirmed password
		if not postData['password'] == postData['password2']:
			print(postData[''])
			errors.append('Passwords must match!')
		#Checks to see if the user has already registered
		user = self.filter(email = postData['email'])
		if user:
			errors.append('Email already in use!')

		#Stores feedback for views.py
		modelResponse = {}
		# If validation failed
		if errors:
			modelResponse['status'] = False
			modelResponse['errors'] = errors
		# If validation passed
		else:
			hashed_password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
			self.create(first_name = postData['first_name'], last_name = postData['last_name'], email=postData['email'], password= hashed_password)
			user = User.objects.get(email=postData['email'])
			modelResponse['status'] = True
			modelResponse['user_id'] = user.id
		print ("Registration Process Complete.  Returned:")
		print (modelResponse)
		return modelResponse

class User(models.Model):
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)
	email = models.EmailField(max_length=254)
	password = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = UserManager()
