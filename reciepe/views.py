from django.shortcuts import render
from rest_framework import viewsets
from  api.models import  User
from rest_framework import permissions, status
# Create your views here.
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Recipe
from .forms import RecipeForm
from userprofile.models import Favorite
#from django.contrib.auth.models import User
from reciepe.serializers import RecipeSerializer
from rest_framework import generics, viewsets
from django.http import JsonResponse
import json
def test(request):
    return JsonResponse({'foo': json.dumps( request.user.id)  })


class ReciepeViewSet(viewsets.ModelViewSet): 
    # define queryset 
    #permission_classes = (permissions.IsAuthenticated, )
    permission_classes = (permissions.AllowAny,)
    queryset = Recipe.objects.all() 
      
    # specify serializer to be used 
    serializer_class = RecipeSerializer

    




class RecipeList(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    def perform_create(self, serializer):
        if self.request.user:
            serializer.save(author=self.request.user)
        else :
            author = User()
            author.username = "ayoub"
            serializer.save(author=author)
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(ReciepeViewSet, self).form_valid(form)

class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer