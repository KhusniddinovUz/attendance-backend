# final_exam/urls.py
from django.urls import path
from .views import CreateFinalMarkView

urlpatterns = [
    path("marks/", CreateFinalMarkView.as_view()),
]