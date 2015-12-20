from django.db import models
from django.utils import timezone

class TrainData(models.Model):

    love = (
        (1, 'Yes'),
        (0, 'No'),
    )
    math = models.IntegerField(max_length=1,choices=love)
    lit = models.IntegerField(max_length=1,choices=love)
    read = models.IntegerField(max_length=1,choices=love)
    high = models.IntegerField(max_length=1,choices=love)
    music = models.IntegerField(max_length=1,choices=love)
    polits = models.IntegerField(max_length=1,choices=love)
    lecpref = models.IntegerField(max_length=3)
