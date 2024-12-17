from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=50, blank=False, unique=True)
    def __str__(self):
        return self.username
# Create your models here.
