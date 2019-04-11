from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
	title = models.CharField(max_length=200)
	summary = models.CharField(max_length=200)

	image = models.ImageField(default='default.jpg', upload_to='post_img')
	date_created = models.DateTimeField(auto_now_add=True, db_index=True)

	def __str__(self):
		return self.title

class Opportunities(models.Model):
	title= models.CharField(max_length=200)
	summary = models.CharField(max_length=200)

	image = models.ImageField(default='default.jpg', upload_to='opp_img')

	def __str__(self):
		return self.title