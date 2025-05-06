from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import Teacher
from django.contrib.auth.password_validation import validate_password

class TeacherRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])

    class Meta:
        model = Teacher
        fields = ('name', 'username', 'password', )

    def create(self, validated_data):
        user = Teacher.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            name=validated_data['name'],
        )
        return user


class TeacherLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True,)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        request  = self.context.get('request')

        user = authenticate(request=request, username=username, password=password)
        if not user or not user.is_active:
            raise serializers.ValidationError('Login parolda xatolik')
        #Block admin login
        if user.is_staff or user.is_superuser:
            raise serializers.ValidationError("Kirish faqat ustozlar uchun")

        attrs['user'] = user
        return attrs


class TeacherProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ["id","username","name", "is_staff"]


class AdminLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = authenticate(
            username=attrs['username'],
            password=attrs['password']
        )
        if not user:
            raise serializers.ValidationError("Login parolda xatolik")
        if not user.is_staff:
            raise serializers.ValidationError("Kirish faqat adminlar uchun")
        attrs['user'] = user
        return attrs