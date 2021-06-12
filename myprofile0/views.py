from django.shortcuts import render

from rest_framework import viewsets, permissions
from .models import Myprofile
from .serializers import MyprofileSerializer
from .serializers import UserSerializer
from   cart0.permissions import IsOwnerOrReadOnly
from cart0.permissions import IsStaffOrTargetUser

import json
import logging


# Create your views here.
class PrfileViewSet(viewsets.ModelViewSet):
    queryset = Myprofile.objects.all().order_by('-first_name')
    serializer_class = MyprofileSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)