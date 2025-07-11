from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import Group, User
from .models import UserProfile, UserInterest
from .serializers import (
    UserProfileSerializer,
    InterestSerializer,
    UserSerializer
)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)


class InterestViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserInterest.objects.all()
    serializer_class = InterestSerializer


class RegisterUserAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        account_type = request.data.get('account_type')

        if serializer.is_valid():
            user = serializer.save()
            UserProfile.objects.create(user=user)

            if account_type:
                try:
                    group = Group.objects.get(name=account_type)
                    group.user_set.add(user)
                except Group.DoesNotExist:
                    return Response(
                        {"error": "Invalid account type"},
                        status=status.HTTP_400_BAD_REQUEST
                    )

            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
