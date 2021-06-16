from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

from rest_framework import routers

# import everything from views


# define the router
router = routers.DefaultRouter()

# define the router path and viewset to be used
router.register(r'reciepevideo', views.ReciepeVideoViewSet)

app_name = 'recipevideo'

urlpatterns = [
    path('t', views.test),
    path('', views.RecipeList.as_view()),
    path('<int:pk>/', views.RecipeDetail.as_view()),
    path('recipes', include(router.urls)),

]