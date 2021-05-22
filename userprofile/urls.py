from django.urls import path
from django.conf.urls import url
from .views import *
from django.views.generic.base import RedirectView
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'userprofile'

urlpatterns = [
    path('profile/<str:pk>/', OtherUserDetail.as_view()), #includes favorites, and friends' recipes for the feed
    path('profile/<str:pk>/favorites/', UserFavoriteList.as_view()),
    path('profile/<str:pk>/friends/', UserFriendsList.as_view()),
    path('profile/search/<str:query>/', UserSearchList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)