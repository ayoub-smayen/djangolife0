from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import ProductSerializer
from rest_framework import permissions, status
from .models import Product


class ProductsViewSet(viewsets.ModelViewSet): 
    # define queryset 
    permission_classes = (permissions.AllowAny,)
    queryset = Product.objects.all() 
      
    # specify serializer to be used 
    serializer_class = ProductSerializer