from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length= 50, default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # body = models.TextField(max_length= 1000000, default='')
    body = RichTextField(blank=True, null=True)
    snippet = models.CharField(max_length=50, default='Click to read blog post')
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return (f'{self.title}')

# Create your models here.
