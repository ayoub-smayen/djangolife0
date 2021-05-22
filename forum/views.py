from django.shortcuts import render

# Create your views here.
#from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from api.models import User
from rest_framework import viewsets, permissions
from .models import Posts, Comments
from .serializers import PostSerializer, CommentSerializer
from .serializers import UserSerializer
from cart0.permissions import IsOwnerOrReadOnly
from cart0.permissions import IsStaffOrTargetUser

import json
import logging

# Create your views here.
class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all().order_by('-name')
    serializer_class = CommentSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all().order_by('-date')
    serializer_class = PostSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    )

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset.filter(owner=user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        # allow non-authenticated user to create via POST
        return (permissions.AllowAny() if self.request.method == 'POST' else IsStaffOrTargetUser()),

    def perform_create(self, serializer):
        password = make_password(self.request.data['password'])
        serializer.save(password=password)

    def perform_update(self, serializer):
        password = make_password(self.request.data['password'])
        serializer.save(password=password)