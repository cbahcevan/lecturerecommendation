from django.db import models
from django.utils import timezone

class TrainData(models.Model):
    math = models.CharField(max_length=1)
    lit = models.CharField(max_length=1)
    read = models.CharField(max_length=1)
    high = models.CharField(max_length=1)
    music = models.CharField(max_length=1)
    polits = models.CharField(max_length=1)
    lecpref = models.CharField(max_length=3,min_length=3)
