from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Course(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField(max_length=1000)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)

class Comment(models.Model):
	course = models.ForeignKey(Course)
	comment = models.TextField(max_length=1000)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)
