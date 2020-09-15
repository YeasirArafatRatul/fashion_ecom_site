from django.db import models
from django.utils.safestring import mark_safe
# Create your models here.


class Setting(models.Model):
    siteTitle = models.CharField(max_length=30)
    sitePhone = models.IntegerField()
    siteLogo = models.ImageField(blank=True, upload_to='siteImages/')
    siteEmail = models.EmailField()
    siteAddress = models.CharField(max_length=250)
    siteAbout = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


class Slider(models.Model):
    image = models.ImageField(blank=True, upload_to='siteImages/slider')
    status = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)
