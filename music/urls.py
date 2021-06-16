from django.conf.urls import url, include
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import  AlbumViewSet , TrackViewset, AlbumList, AlbumDetail
router = DefaultRouter()
router.register(r'tracks', TrackViewset)
router.register(r'albums', AlbumViewSet)


urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^music/', include(router.urls)),
    path('', AlbumList.as_view()),
    path('<int:pk>/', AlbumDetail.as_view()),
    #rl(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]