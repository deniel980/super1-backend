from django.db import models
from django.contrib.auth.models import User


class Users(models.Model):
    username = models.CharField(max_length=63, unique=True)


class FavouriteCountry(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    country_id = models.CharField(max_length=5)
    notes = models.CharField(max_length=255)
