from django.db import models


class Book(models.Model):
	author = models.CharField(max_length=250)
	country = models.CharField(max_length=50)
	image_link = models.FileField()
	language = models.CharField(max_length=50)
	link = models.URLField(default='')
	pages = models.IntegerField(default=0)
	title = models.CharField(max_length=250)
	year = models.IntegerField(default=0)

	def __str__(self):
		return self.title
