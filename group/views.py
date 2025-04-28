from rest_framework import generics, permissions
from .serializers import GroupSerializer
from .models import Group

class GroupView(generics.ListAPIView):
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Group.objects.all()