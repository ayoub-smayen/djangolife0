from django.conf.urls import url, include
from rest_framework import routers
from .views import UserViewSet2 , RegisterViewset

router = routers.DefaultRouter()
router.register(r'mprod', UserViewSet2)

router.register(r'reg1', RegisterViewset)

urlpatterns = [
    #url(r'^', include(router.urls)),
    #url(r'^auth/', include('rest_auth.urls')),
]