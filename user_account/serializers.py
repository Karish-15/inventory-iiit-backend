from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User

class UserTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['user_id'] = user.id
        token['username'] = user.username
        return token

class userRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'contact', 'misc_details', 'is_admin', 'is_staff']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
            )
        user.first_name = validated_data['first_name']
        user.last_name = validated_data['last_name']
        user.contact = validated_data.get('contact', "")
        user.misc_details = validated_data.get('misc_details', "")
        user.is_admin = validated_data.get('is_admin', False)
        user.is_staff = validated_data.get('is_staff', False)
        user.save()

        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'contact', 'misc_details', 'is_admin', 'is_staff']