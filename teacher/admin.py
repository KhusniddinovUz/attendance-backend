from django.contrib import admin
from teacher.models import Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = (
        "name",
    )
    search_fields = ("name",)