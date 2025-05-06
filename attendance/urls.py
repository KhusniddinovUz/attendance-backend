from django.urls import path
from .views import AttendanceListView, UpdateAttendanceStatusByStudentLesson, AttendanceListDashboardView

urlpatterns = [
    path('get/', AttendanceListView.as_view(), name='get-attendance'),
    path('update/', UpdateAttendanceStatusByStudentLesson.as_view(), name='update-attendance'),
    path('dashboard/', AttendanceListDashboardView.as_view(), name='dashboard-attendance'),

]