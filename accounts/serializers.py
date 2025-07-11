from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile, UserInterest


class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInterest
        fields = ['id', 'name']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    interests = InterestSerializer(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = [
            'id',
            'user',
            'bio',
            'phone',
            'website',
            'interests',
            'profile_image',
            'full_name_displayed',
            'date_created',
        ]
