from datetime import datetime
from distutils.command.upload import upload
from email.mime import image
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    text = models.TextField()
    image = models.ImageField(upload_to = "event_image/")
