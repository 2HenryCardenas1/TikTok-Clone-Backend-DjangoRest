from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from users.api.serializers import (UserRegisterSerializer, UserSerializer,
                                   UserUpdateSerializer)
from users.models import User


class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserMeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

# This view is used to update the user data
    def put(self, request):
        if 'password' in request.data:
            password = request.data['password']
            # Encrypt the password
            request.data['password'] = make_password(password)

        serializer = UserUpdateSerializer(
            request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    http_method_names = ['get']
    filter_backends = [OrderingFilter, SearchFilter]
    ordering = ['-date_joined']
    search_fields = ['username']
