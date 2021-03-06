from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    friend = models.ManyToManyField("self",blank = True,related_name = "friend")


    class Meta:
        verbose_name_plural = 'CustomUser'

# Create your models here.
