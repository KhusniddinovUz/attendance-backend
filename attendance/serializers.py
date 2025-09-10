from rest_framework import serializers
from .models import Attendance

class AttendanceSerializer(serializers.ModelSerializer):
    student_name = serializers.SerializerMethodField()
    lesson_name = serializers.SerializerMethodField()
    teacher_name = serializers.SerializerMethodField()
    class Meta:
        model = Attendance
        fields = ["student_name", "lesson_name", "status", "date", "teacher_name"]

    def get_teacher_name(self, obj):
        teacher = obj.lesson_name.teacher_name.name
        is_late = obj.lesson_name.is_late
        return teacher if not is_late else f"{teacher} (LATE)"

    def get_student_name(self, obj):
        return obj.student_name.name

    def get_lesson_name(self, obj):
        return obj.lesson_name.para


class AttendanceStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['status']