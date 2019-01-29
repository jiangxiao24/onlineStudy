from django.db import models

# Create your models here.


class UserInfo(models.Model):
    username = models.CharField(max_length=64)
    age = models.CharField(max_length=64)
    sex = models.CharField(max_length=64)