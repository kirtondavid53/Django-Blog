from django.db import models
from datetime import datetime

class Post(models.Model):
    title = models.CharField(max_length= 50, default='')
    body = models.CharField(max_length= 1000000, default='')
    date_created = models.DateTimeField(default=datetime.now, blank=True)

# Create your models here.
