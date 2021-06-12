from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from rest_framework import generics, permissions
from rest_framework.response import Response
#from knox.models import AuthToken
from rest_framework import permissions, status
from .serializers import RegisterSerializer, LoginSerializer
from userprofile.serializers import UserSerializer
#from core.serializers import UserSerializer

class RegisterDetail(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": UserSerializer(user, context={'request': request}).data
            #AuthToken.objects.create(user)[1]
        })

class LoginDetail(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": UserSerializer(user, context={'request': request}).data
            #AuthToken.objects.create(user)[1]
        })