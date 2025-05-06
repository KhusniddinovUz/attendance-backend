from django.urls import path
from .views import RegisterTeacherView, LoginTeacherView, TeacherProfileView, AdminLoginView

urlpatterns = [
    path('register/', RegisterTeacherView.as_view(), name='register'),
    path('login/', LoginTeacherView.as_view(), name='login'),
    path('profile/', TeacherProfileView.as_view(), name='profile'),
    path('admin-login/', AdminLoginView.as_view(), name='admin-login'),

]
