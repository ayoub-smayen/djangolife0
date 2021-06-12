from django.conf.urls import url
from django.urls import include, path
# import routers
from rest_framework import routers

# import everything from views
from .views import *

# define the router
router = routers.DefaultRouter()

# define the router path and viewset to be used
router.register(r'story', PoststoryViewSet)

router.register(r'storyimage',PostImageViewSet)

# specify URL Path for rest_framework
urlpatterns = [
    url(r'^stories/', include(router.urls)),
]