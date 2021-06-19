from django.shortcuts import render

# Create your views here.
from .models import Questions, Choice
from .serializers import QuestionSerializer, ChoiceSerializer
from rest_framework import viewsets
class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Questions.objects.all()
class ChoiceViewSet(viewsets.ModelViewSet):
    serializer_class = ChoiceSerializer
    queryset = Choice.objects.all()