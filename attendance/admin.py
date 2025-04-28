from django.contrib import admin
from .models import Attendance

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = (
        "student_name",
        "lesson_name",
        "status",
    )

    # ───────── filters in the sidebar ─────────
    list_filter = (
        "student_name",  # dropdown of students
        "lesson_name",  # dropdown of lessons
    )

    # Optional: make queries faster and enable the search box
    list_select_related = ("student_name", "lesson_name")
    search_fields = (
        "student_name__name",
        "lesson_name__name",
    )