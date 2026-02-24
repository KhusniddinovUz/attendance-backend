from django.db import models
from django.conf import settings

class FinalMark(models.Model):
    student = models.ForeignKey("student.Student", on_delete=models.CASCADE, related_name="final_marks")
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="given_final_marks")
    mark = models.DecimalField(max_digits=5, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["student", "teacher"], name="uniq_finalmark_student_teacher")
        ]

    def __str__(self):
        t = self.teacher.name
        return f"{self.student.name} - {t}: {self.mark}"