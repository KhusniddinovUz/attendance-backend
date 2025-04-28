from django.db import models

class Attendance(models.Model):
    student_name = models.ForeignKey('student.Student', on_delete=models.CASCADE, related_name='attendances')
    lesson_name = models.ForeignKey('lesson.Lesson', on_delete=models.CASCADE, related_name='attendances')
    status = models.CharField(max_length=1, default="-")
    date = models.DateField(blank=True, null=True)