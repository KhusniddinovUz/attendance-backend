from django.db import models
from django.utils import timezone


class Lesson(models.Model):
    group_name = models.ForeignKey('group.Group', on_delete=models.CASCADE, related_name='lessons')
    para = models.CharField(max_length=1, blank=False)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        formated_date = self.date.strftime("%B %d")
        return f"{self.group_name.name} - {formated_date} - {self.para}chi para"