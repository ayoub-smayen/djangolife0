from .views import ProductsViewSet, OrdersViewSet, UserViewSet
from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include
router = DefaultRouter()
router.register(r'products', ProductsViewSet)
router.register(r'orders', OrdersViewSet)
router.register(r'users1', UserViewSet)

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^cart0/', include(router.urls)),
    #rl(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]