from django.db import models
from group.models import Group

class Student(models.Model):
    name = models.CharField(max_length=200)
    group_name = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.name