from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/attendance/", include("attendance.urls")),
    path("api/teacher/", include("teacher.urls")),
    path("api/group/", include("group.urls")),
    path("api/lesson/", include("lesson.urls")),
]
