from django.db import models
from django.utils import timezone

class TrainedOutput(models.Model):
    math = models.CharField(max_length=1)
    lit = models.CharField(max_length=1)
    read = models.CharField(max_length=1)
    high = models.CharField(max_length=1)
    music = models.CharField(max_length=1)
    polits = models.CharField(max_length=1)
