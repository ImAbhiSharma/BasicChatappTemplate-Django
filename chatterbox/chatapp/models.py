from django.db import models


class AppUser(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    last_seen = models.DateField(null=True)
    objects = models.Manager()
