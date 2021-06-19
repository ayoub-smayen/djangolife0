from django.conf.urls import url
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import  QuestionViewSet , ChoiceViewSet


from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'question', QuestionViewSet, basename='question')
router.register(r'choice', ChoiceViewSet, basename='choice')
urlpatterns = [
    url(r'^api/polls/', include(router.urls)),

]