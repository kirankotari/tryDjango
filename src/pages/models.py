from django.db import models
from django.contrib.auth.models import User


class Location(models.Model):
    location = models.CharField(max_length=120)

    def __str__(self):
        return 'Location: {}'.format(self.location)


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    location = models.CharField(max_length=120)
    manager = models.BooleanField(default=False)
