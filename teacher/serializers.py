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
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Incorrect Credentials')


class TeacherProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ["id","username","name"]