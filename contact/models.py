from django.db import models

# Create your models here.


class ContactData(models.Model):
    phone = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return str(self.id)
