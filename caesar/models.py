from django.db import models


class Message(models.Model):
    text = models.TextField()
    rotate = models.IntegerField(default=0)
    date = models.DateField()
