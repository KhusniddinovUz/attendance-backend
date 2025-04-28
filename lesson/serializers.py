from .models import Lesson
from rest_framework import serializers

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"
        extra_kwargs = {
            "teacher": {"read_only": True},
        }