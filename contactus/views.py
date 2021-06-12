from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import ContactUsSerializer

from .models import ContactUs
from rest_framework import permissions, status

class ContactusViewSet(viewsets.ModelViewSet): 
    # define queryset 
    permission_classes = (permissions.AllowAny,)
    queryset = ContactUs.objects.all() 
      
    # specify serializer to be used 
    serializer_class = ContactUsSerializer