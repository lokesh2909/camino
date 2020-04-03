from django.db import models

# Create your models here.
class users(models.Model):
    name = models.CharField(max_length = 25)
    password = models.CharField(max_length = 16)

class userDetails(models.Model):
    weight = models.IntegerField()
