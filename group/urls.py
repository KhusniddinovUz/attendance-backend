from django.urls import path
from .views import GroupView, GroupStudentsView

urlpatterns = [
    path('get/', GroupView.as_view(), name='get-all-groups'),
    path('groups/<int:group_id>/students/', GroupStudentsView.as_view(), name='group-students'),
]
