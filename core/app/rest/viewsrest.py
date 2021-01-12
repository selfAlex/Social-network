from django.contrib.auth import get_user_model

from rest_framework import generics

from . import serializers


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.UserSerializer
    queryset = get_user_model().objects.all()


class UserListView(generics.ListAPIView):
    serializer_class = serializers.UserSerializer
    queryset = get_user_model().objects.all()


class UserCreateView(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer
