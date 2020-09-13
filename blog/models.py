from django.db import models
import datetime

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=300, blank=False, null=False)
    image = models.ImageField()
    description = models.TextField()
    datetime = models.DateTimeField(
        default=datetime.datetime.today)
