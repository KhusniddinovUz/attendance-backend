from django.db import models
from django.utils import timezone


class Lesson(models.Model):
    name = models.CharField(max_length=200)
    group_name = models.ForeignKey('group.Group', on_delete=models.CASCADE, related_name='lessons')
    date = models.DateField(default=timezone.now)
    para = models.CharField(max_length=1, blank=False)

    def __str__(self):
        formated_date = self.date.strftime("%B %d")
        return f"{self.group_name.name} - {self.name} - {formated_date} - {self.para}chi para"