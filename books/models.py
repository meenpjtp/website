from django.db import models

class Book(models.Model):
	author = models.CharField(max_length=250)
	country = models.CharField(max_length=50)
	image_link = models.CharField(max_length=1000)
	language = models.CharField(max_length=50)
	link = models.CharField(max_length=1000)
	pages = models.CharField(max_length=5)
	title = models.CharField(max_length=250)
	year = models.CharField(max_length=4)
		
