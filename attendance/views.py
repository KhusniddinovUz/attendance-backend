from rest_framework import generics
from .models import Attendance
from .serializers import AttendanceSerializer, AttendanceStatusUpdateSerializer


class AttendanceListView(generics.ListAPIView):
    serializer_class = AttendanceSerializer
    queryset = Attendance.objects.all()
    permission_classes = []


    def get_queryset(self):
        queryset = super().get_queryset()
        lesson_name = self.request.query_params.get('lesson_name')
        group_name = self.request.query_params.get('group_name')
        date = self.request.query_params.get('date')
        para = self.request.query_params.get('para')

        if lesson_name:
            queryset = queryset.filter(lesson_name__name=lesson_name)

        if group_name:
            queryset = queryset.filter(student_name__group_name=group_name)

        if date:
            queryset = queryset.filter(date=date)

        if para:
            queryset = queryset.filter(lesson_name__para=para)

        return queryset


class UpdateAttendanceStatusByStudentLesson(generics.UpdateAPIView):
    permission_classes = []
    serializer_class = AttendanceStatusUpdateSerializer
    lookup_fields = None

    def get_object(self):
        student_name = self.request.data.get('student_name')
        lesson_name = self.request.data.get('lesson_name')
        para = self.request.data.get('para')

        if not all([student_name, lesson_name]):
            raise ValueError("Student name, lesson and para must be provided.")

        try:
            attendance = Attendance.objects.get(student_name__name=student_name,
                                                lesson_name__name=lesson_name,
                                                lesson_name__para=para,)
            return attendance
        except Attendance.DoesNotExist:
            raise ValueError("Attendance record not found.")
