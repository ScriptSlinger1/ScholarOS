from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomStudent(AbstractUser):
    username = models.CharField(max_length = 100, unique = True)
    email = models.EmailField(max_length = 100, unique = True)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    bio = models.TextField()