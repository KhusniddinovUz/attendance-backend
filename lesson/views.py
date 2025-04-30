from rest_framework.response import Response
from .models import Lesson
from rest_framework import generics, permissions
from .serializers import LessonSerializer
from attendance.models import Attendance
from attendance.serializers import AttendanceSerializer


class CreateLessonView(generics.CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        group = serializer.data['group_name']
        lesson_name = serializer.data['name']
        attendance_queryset = Attendance.objects.all()
        attendance_list = attendance_queryset.filter(lesson_name__name=lesson_name,
                                                     student_name__group_name=group)
        custom_data = AttendanceSerializer(attendance_list, many=True).data
        return Response(custom_data)
