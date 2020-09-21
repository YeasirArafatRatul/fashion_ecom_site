from django.db import models
import datetime
from django.utils.safestring import mark_safe
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=300, blank=False, null=False)
    image = models.ImageField()
    description = models.TextField()
    datetime = models.DateTimeField(
        default=datetime.datetime.today)

    class Meta:
        ordering = ['-datetime']

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" heights ="50" width="40" />'.format(self.image.url))
    image_tag.short_description = 'Image'
