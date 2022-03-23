from django.db import models
from django.utils import timezone



class member(models.Model):
    name = models.CharField(max_length = 10)
    def __str__(self):
        return self.name


class event(models.Model):
    date = models.DateField()
    name = models.CharField(max_length = 50)
    Member = models.ManyToManyField(member)
    def __str__(self):
        return self.name


class pay(models.Model):
    datetime = models.DateTimeField(default=timezone.now)
    payer = models.ForeignKey(member,on_delete = models.CASCADE,related_name = "payer")
    payee = models.ManyToManyField(member,related_name = "payee")
    event = models.ForeignKey(event,on_delete = models.CASCADE)
    price = models.PositiveIntegerField()
    purpose = models.CharField(max_length = 50)

    def __str__(self):
        return self.purpose




# Create your models here.
