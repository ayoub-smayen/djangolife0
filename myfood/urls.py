from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from  .views import blog_view,detail_view,chatter

urlpatterns = [
   # path('admin/', admin.site.urls),
    path('', blog_view, name='blog'),
    path('<int:id>/', detail_view, name='detail'),
    path('chatter/',chatter,name="foodchatter")
]