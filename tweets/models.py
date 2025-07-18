from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100, blank=False)
    author = models.CharField(max_length=100, blank=False)
    publisher = models.CharField(max_length=100)
    pages = models.IntegerField()
    pages_count = models.IntegerField()

class Movies(models.Model):
    title = models.CharField(max_length=100, blank=False)
    year = models.CharField(max_length=4, blank=False)
    genre = models.CharField(max_length=100, blank=False)
    actor = models.CharField(max_length=100, blank=False)
    poster = models.CharField(max_length=100, blank=False)

