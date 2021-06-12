from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import ProfileSerializer,UpdateUserSer,UpdateProfileSer,UpdateImageProfileSer
from rest_framework import permissions, status
from .models import Profile


class ProfileViewSet(viewsets.ModelViewSet): 
    # define queryset 
    permission_classes = (permissions.AllowAny,)
    queryset = Profile.objects.all() 
      
    # specify serializer to be used 
    serializer_class = ProfileSerializer


class UpdateUserViewSet(viewsets.ModelViewSet): 
    # define queryset 
    permission_classes = (permissions.AllowAny,)
    queryset = Profile.objects.all() 
      
    # specify serializer to be used 
    serializer_class = UpdateUserSer



class UpdateProfileViewSet(viewsets.ModelViewSet): 
    # define queryset 
    permission_classes = (permissions.AllowAny,)
    
    queryset = Profile.objects.all() 
      
    # specify serializer to be used 
    serializer_class = UpdateProfileSer


class UpdateImgViewSet(viewsets.ModelViewSet): 
    # define queryset 
    
    queryset = Profile.objects.all() 
      
    # specify serializer to be used 
    serializer_class = UpdateImageProfileSer