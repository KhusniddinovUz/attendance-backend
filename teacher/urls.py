from django.urls import path
from .views import RegisterTeacherView, LoginTeacherView

urlpatterns = [
    path('register/', RegisterTeacherView.as_view(), name='register'),
    path('login/', LoginTeacherView.as_view(), name='login'),
]
