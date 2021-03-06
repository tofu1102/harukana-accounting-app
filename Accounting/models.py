from django.db import models
from django.utils import timezone
from accounts.models import CustomUser as member
import uuid

"""
class member(models.Model):
    name = models.CharField(max_length = 10)
    def __str__(self):
        return self.name
"""

class event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField(auto_now_add = True)
    name = models.CharField(max_length = 50)
    Member = models.ManyToManyField(member,blank = True,related_name = "Member")
    creater = models.ForeignKey(member,on_delete = models.CASCADE, related_name = "creater", null = True)
    is_active = models.BooleanField(default = True)
    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name


class pay(models.Model):
    datetime = models.DateTimeField(auto_now_add = True)
    payer = models.ForeignKey(member,on_delete = models.CASCADE,related_name = "payer")
    payee = models.ManyToManyField(member,related_name = "payee")
    event = models.ForeignKey(event,on_delete = models.CASCADE)
    price = models.PositiveIntegerField()
    purpose = models.CharField(max_length = 50)
    auther = models.ForeignKey(member,on_delete = models.CASCADE,related_name = "auther",blank = True)

    def __str__(self):
        return self.purpose




# Create your models here.
