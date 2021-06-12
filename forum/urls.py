from .views import CommentsViewSet, PostsViewSet, UserViewSet
from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include
router = DefaultRouter()
router.register(r'comments', CommentsViewSet)
router.register(r'posts', PostsViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^forum/', include(router.urls)),
    #rl(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]