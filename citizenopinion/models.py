from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
	title = models.CharField(max_length = 200)
	text = models.TextField()
	create_date = models.DateTimeField(default=timezone.now)
						#Место откуда фото качаются
#	image = models.ImageField(upload_to = '/',height_field = 100, Width_field = 100)
	up = models.IntegerField()
	dis = models.IntegerField()
	def __str__ (self):
		 return Post

