from django.db import models
from django.contrib.auth.models import AbstractUser

class Teacher(AbstractUser):
    name = models.CharField(max_length=200)
    subjects = models.TextField(blank=True)