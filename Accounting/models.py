from django.db import models
from django.utils import timezone
from accounts.models import CustomUser as member

"""
class member(models.Model):
    name = models.CharField(max_length = 10)
    def __str__(self):
        return self.name
"""

class event(models.Model):
    date = models.DateField(auto_now_add = True)
    name = models.CharField(max_length = 50)
    Member = models.ManyToManyField(member,blank = True)
    def __str__(self):
        return self.name


class pay(models.Model):
    datetime = models.DateTimeField(auto_now_add = True)
    payer = models.ForeignKey(member,on_delete = models.CASCADE,related_name = "payer")
    payee = models.ManyToManyField(member,related_name = "payee")
    event = models.ForeignKey(event,on_delete = models.CASCADE)
    price = models.PositiveIntegerField()
    purpose = models.CharField(max_length = 50)

    def __str__(self):
        return self.purpose




# Create your models here.
