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


        queryset = queryset.select_related('student_name').order_by('student_name__name')
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
        all_records = all_records.select_related('student_name').order_by('student_name__name')
        return Response(AttendanceSerializer(all_records, many=True).data,
                        status=status.HTTP_200_OK)



class AttendanceListDashboardView(generics.ListAPIView):
    serializer_class = AttendanceSerializer
    queryset = Attendance.objects.all()
    permission_classes = []

    def get_queryset(self):
        qs = super().get_queryset()
        group_name = self.request.query_params.get('group_name')
        start_date = self.request.query_params.get('start_date')
        end_date   = self.request.query_params.get('end_date')

        if group_name:
            qs = qs.filter(student_name__group_name=group_name)

        # if both bounds are present, use __range; otherwise fall back
        if start_date and end_date and end_date != "1970-01-01":
            qs = qs.filter(date__range=[start_date, end_date])
        elif start_date:
            qs = qs.filter(date__gte=start_date)

        qs = qs.select_related('student_name').order_by('student_name__name')
        return qs