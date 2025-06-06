from rest_framework import serializers
from .models import Attendance

class AttendanceSerializer(serializers.ModelSerializer):
    student_name = serializers.SerializerMethodField()
    lesson_name = serializers.SerializerMethodField()
    teacher_name = serializers.CharField(source='lesson_name.teacher_name.name')
    class Meta:
        model = Attendance
        fields = ["student_name", "lesson_name", "status", "date", "teacher_name"]

    def get_student_name(self, obj):
        return obj.student_name.name

    def get_lesson_name(self, obj):
        return obj.lesson_name.para


class AttendanceStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['status']