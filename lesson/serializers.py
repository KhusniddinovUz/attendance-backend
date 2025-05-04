from .models import Lesson
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ["id", "group_name", "teacher_name", "para", "date",]
        validators = [
            UniqueTogetherValidator(
                queryset=Lesson.objects.all(),
                fields=["group_name", "para", "date"],
                message="Tanlangan dars mavjud",
            )
        ]
        extra_kwargs = {
            "teacher": {"read_only": True},
        }