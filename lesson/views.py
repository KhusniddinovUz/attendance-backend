from .models import Lesson
from rest_framework import generics, permissions
from .serializers import LessonSerializer

class CreateLessonView(generics.CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated]
