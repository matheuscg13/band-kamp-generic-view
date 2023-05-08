from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, max_length=120)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
