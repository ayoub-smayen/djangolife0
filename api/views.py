from django.contrib.auth.hashers import make_password
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from django.contrib.auth.models import  User

from cart0.permissions import IsStaffOrTargetUser
from .serializers import UserSerializer

from rest_framework.permissions import AllowAny
from .models import  User
#from django.contrib.auth.models import  User
from api.serializers import UserSerializer, RegisterSerializer
# Also add these imports
from .permissions import IsLoggedInUserOrAdmin, IsAdminUser
from rest_framework.response import  Response
class RegisterViewset(viewsets.ModelViewSet):
    queryset =  User.objects.all()
    serializer_class =  RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            #"token": AuthToken.objects.create(user)[1]
        })

    def get_permissions(self):
        # allow non-authenticated user to create via POST
        return (AllowAny() if self.request.method == 'POST' else IsStaffOrTargetUser()),

    def perform_create(self, serializer):
        password = make_password(self.request.data['password'])
        serializer.save(password=password)

    def perform_update(self, serializer):
        password = make_password(self.request.data['password'])
        serializer.save(password=password)

class UserViewSet2(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
