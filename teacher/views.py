from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import TeacherRegisterSerializer,TeacherLoginSerializer, TeacherProfileSerializer
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.models import AuthToken

class RegisterTeacherView(generics.CreateAPIView):
    serializer_class = TeacherRegisterSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
            "user": {
                "id": user.id,
                "username": user.username,
                "name": user.name,
            },
            "token": AuthToken.objects.create(user)[1]
        })



class LoginTeacherView(generics.GenericAPIView):
    serializer_class = TeacherLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        return Response({
            "user": {
                "id": user.id,
                "username": user.username,
                "name": user.name,
            },
            "token": AuthToken.objects.create(user)[1]
        })


class TeacherProfileView(generics.RetrieveAPIView):
    serializer_class = TeacherProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user