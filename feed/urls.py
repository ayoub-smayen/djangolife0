from django.urls import path
from rest_framework import routers
from . import api

router = routers.DefaultRouter()

router.register('feedcomment' ,api.FeedCommentViewSet ,basename='feedcomments')
#router = routers.DefaultRouter()

router.register('feedlikes' ,api.FeedLikeViewSet ,basename='feedlikes')
router.register('feed' ,api.FeedViewSet ,basename='posts')

urlpatterns = router.urls
#urlpatterns += router.urls
#urlpatterns += router.urls