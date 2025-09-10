from rest_framework.response import Response
from .models import Lesson
from rest_framework import generics, permissions
from .serializers import LessonSerializer
from attendance.models import Attendance
from attendance.serializers import AttendanceSerializer
from datetime import time
from django.utils import timezone
from zoneinfo import ZoneInfo

class CreateLessonView(generics.CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        tz = ZoneInfo('Asia/Tashkent')
        now_uz = timezone.now().astimezone(tz).time() # Current time in Tashkent
        is_teacher_late = False
        para = request.data.get('para')
        if para == "1":
            is_teacher_late = now_uz >= time(9, 15) or now_uz <= time(9, 0)
        elif para == "2":
            is_teacher_late = now_uz >= time(10, 35) or now_uz <= time(10, 30)
        elif para == "3":
            is_teacher_late = now_uz >= time(13, 5) or now_uz <= time(13, 0)
        serializer.save(is_late=is_teacher_late)



        group = serializer.data['group_name']
        para = serializer.data['para']
        date = serializer.data['date']
        attendance_queryset = Attendance.objects.all()
        attendance_list = attendance_queryset.filter(student_name__group_name=group, lesson_name__para=para, date=date)
        attendance_list = attendance_list.select_related('student_name').order_by('student_name__name')
        custom_data = AttendanceSerializer(attendance_list, many=True).data
        return Response(custom_data)
