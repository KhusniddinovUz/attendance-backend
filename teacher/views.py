from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import TeacherRegisterSerializer, TeacherLoginSerializer, \
    TeacherProfileSerializer, AdminLoginSerializer
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
                "is_staff": user.is_staff,
            },
            "token": AuthToken.objects.create(user)[1]
        })


class LoginTeacherView(generics.GenericAPIView):
    serializer_class = TeacherLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        return Response({
            "user": {
                "id": user.id,
                "username": user.username,
                "name": user.name,
                "is_staff": user.is_staff,
            },
            "token": AuthToken.objects.create(user)[1]
        })

    def handle_exception(self, exc):
        if isinstance(exc, AuthenticationFailed):
            return Response("Login yoki parol noto'gri")
        return super().handle_exception(exc)


class TeacherProfileView(generics.RetrieveAPIView):
    serializer_class = TeacherProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class AdminLoginView(generics.GenericAPIView):
    serializer_class = AdminLoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # At this point we know it’s a staff user
        user = serializer.validated_data['user']

        return Response({
            "user": {
                "id": user.id,
                "username": user.username,
                "name": user.name,
                "is_staff": user.is_staff,
            },
            "token": AuthToken.objects.create(user)[1]})
