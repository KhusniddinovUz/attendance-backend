from django.urls import path
from .views import CreateLessonView

urlpatterns = [
    path('create/', CreateLessonView.as_view(), name='create-lesson'),
]
