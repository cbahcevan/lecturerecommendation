from django.db import models
from django.utils import timezone

class TrainData(models.Model):

    love = (
        (1, 'Yes'),
        (0, 'No'),
    )
    math = models.IntegerField(choices=love)
    lit = models.IntegerField(choices=love)
    read = models.IntegerField(choices=love)
    high = models.IntegerField(choices=love)
    music = models.IntegerField(choices=love)
    polits = models.IntegerField(choices=love)
    lecpref = models.CharField(max_length=3)

class Lectures(models.Model):
    lecid = models.CharField(max_length=6)
    lecname = models.CharField(max_length=100)
    lecexp = models.TextField()