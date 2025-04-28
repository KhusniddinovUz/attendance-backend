from django.urls import path
from .views import GroupView

urlpatterns = [
    path('get/', GroupView.as_view(), name='get-all-groups'),
]
