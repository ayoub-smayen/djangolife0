from django.shortcuts import render

# Create your views here.
from cart0.permissions import IsOwnerOrReadOnly
from cart0.permissions import IsStaffOrTargetUser

from rest_framework import  viewsets , permissions

from .models import Poststory, PostImage
from .serializers import PoststorySerializer, PostImageSerializer

class PoststoryViewSet(viewsets.ModelViewSet):
    queryset = Poststory.objects.all().order_by('-story_date')
    serializer_class = PoststorySerializer
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




class PostImageViewSet(viewsets.ModelViewSet):
    queryset = PostImage.objects.all()
    serializer_class =PostImageSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    )

    # def get_queryset(self):
    #     user = self.request.user
    #     queryset = self.queryset.filter(owner=user)
    #     return queryset
    #
    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)