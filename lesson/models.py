from django.db import models
from django.utils import timezone


class Lesson(models.Model):
    name = models.CharField(max_length=200)
    group_name = models.ForeignKey('group.Group', on_delete=models.CASCADE, related_name='lessons')
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.group_name.name} - {self.date}"