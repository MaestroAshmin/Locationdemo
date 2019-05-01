from django.db import models
from django.contrib.auth.models import User


class Detail(models.Model):
    name = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    longitude = models.DecimalField(max_digits=10, decimal_places=4, default=None,null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=4, default=None,null=True)

    def __str__(self):
        return self.name

