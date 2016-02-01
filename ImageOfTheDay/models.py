from __future__ import unicode_literals
from time import time
from django.db import models

def get_upload_file_name(instance,filename):
	return "uploaded_files/%s_%s" %(str(time()).replace('.','_'),filename)

# Create your models here.
class ImageOfTheDay(models.Model):
	image = models.FileField(upload_to=get_upload_file_name)
	date = models.DateTimeField()
	title = models.CharField(max_length=200)
	subtitle = models.CharField(max_length=200)
	decription = models.TextField()