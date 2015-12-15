
from django.db import models
from django.utils import timezone

class Trainer(models.Model):
    name = models.ForeignKey('auth.User')
    password = models.CharField(max_length=20,min_length=5)
    

