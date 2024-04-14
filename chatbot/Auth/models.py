import datetime
from django.db import models
from django.contrib.auth.models import User
class Book(models.Model):
    name=models.CharField(max_length=100, default='Default')
    destination= models.CharField(max_length=50, default='Default')
    source= models.CharField(max_length=50, default='Default')
    seatType= models.CharField(max_length=50, default='Default')
    Date1 = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return self.name