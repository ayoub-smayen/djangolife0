# from django.urls import path
# from .views import current_user, UserList
#
# urlpatterns = [
#     path('current_user/', current_user),
#     path('users/', UserList.as_view())
# ]

from .views import current_user, UserList
from rest_framework import routers
from .views import UserViewSet
from django.conf.urls import  url,include

router = routers.DefaultRouter()
router.register(r'userprofiles', UserViewSet)
urlpatterns = [
    url(r'^current_user/', current_user),
    url(r'^users2/', UserList.as_view()),
    url(r'^', include(router.urls)),
]