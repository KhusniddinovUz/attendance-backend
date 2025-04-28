from django.urls import path
from .views import AttendanceListView, UpdateAttendanceStatusByStudentLesson

urlpatterns = [
    path('get/', AttendanceListView.as_view(), name='get-attendance'),
    path('update/', UpdateAttendanceStatusByStudentLesson.as_view(), name='update-attendance'),
]