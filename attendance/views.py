from rest_framework import generics, status
from rest_framework.response import Response
from .models import Attendance
from .serializers import AttendanceSerializer, AttendanceStatusUpdateSerializer


class AttendanceListView(generics.ListAPIView):
    serializer_class = AttendanceSerializer
    queryset = Attendance.objects.all()
    permission_classes = []

    def get_queryset(self):
        queryset = super().get_queryset()
        group_name = self.request.query_params.get('group_name')
        date = self.request.query_params.get('date')
        para = self.request.query_params.get('para')

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
        para = self.request.data.get('para')
        date = self.request.data.get('date')

        if not all([student_name, para, date]):
            raise ValueError("Student name, para and date must be provided.")

        try:
            attendance = Attendance.objects.get(student_name__name=student_name,
                                                lesson_name__para=para,
                                                date=date, )
            return attendance
        except Attendance.DoesNotExist:
            raise ValueError("Attendance record not found.")

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # ✅ Return all Attendance records instead of just the updated one
        group_name = self.request.data.get('group_name')
        para = self.request.data.get('para')
        date = self.request.data.get('date')
        all_records = Attendance.objects.all()
        all_records = all_records.filter(student_name__group_name=group_name, date=date,
                                         lesson_name__para=para)
        return Response(AttendanceSerializer(all_records, many=True).data,
                        status=status.HTTP_200_OK)
