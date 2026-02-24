from rest_framework import generics, permissions
from .serializers import GroupSerializer
from .models import Group
from student.models import Student
from student.serializers import StudentListSerializer

class GroupView(generics.ListAPIView):
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Group.objects.all()


class GroupStudentsView(generics.ListAPIView):
    serializer_class = StudentListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        group_id = self.kwargs["group_id"]
        return Student.objects.filter(group_name_id=group_id).order_by("name")