from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction
from .models import Lesson
from attendance.models import Attendance

#Post-save Signal
@receiver(post_save, sender=Lesson)
def create_attendance_rows(sender, instance, created, **kwargs):
    if not created:
        return

    students = instance.group_name.students.all()

    attendance_rows = [
        Attendance(
            student_name=s,
            lesson_name=instance,
            status='+',
            date=instance.date,
        )
        for s in students
    ]

    transaction.on_commit(lambda: Attendance.objects.bulk_create(attendance_rows))
