from django.db import models
from django.utils import timezone


class Lesson(models.Model):
    group_name = models.ForeignKey('group.Group', on_delete=models.CASCADE, related_name='lessons')
    teacher_name = models.ForeignKey('teacher.Teacher', on_delete=models.CASCADE, related_name='lessons', null=True, blank=True)
    para = models.CharField(max_length=1, blank=False)
    date = models.DateField(default=timezone.now)
    is_late = models.BooleanField(default=False)

    def __str__(self):
        formated_date = self.date.strftime("%B %d")
        teacher_display_name = f"{self.teacher_name.name} (LATE)" if self.is_late else self.teacher_name.name
        return f"{self.group_name.name} - {formated_date} - {self.para}chi para - {teacher_display_name}"