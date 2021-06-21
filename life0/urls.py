"""life0 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import  verify_jwt_token, refresh_jwt_token
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('salesman.urls')),
    url(r'^prod/',include('shop.urls')),
    url(r'^', include('chat.urls')),
    url(r'^cart/',include("cart0.urls")),
    url(r'^forums/',include("forum.urls")),
    url(r'^contact-us', include('contactus.urls')),
    url(r'^token-auth/', obtain_jwt_token),
    url(r'^core/',include('core.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^profile',include('myprofile0.urls')),
    #url(r'^apiprof/',include('api.urls')),
    url(r'^api/auth/', include('registration.urls')),
     url(r'^account/',include('account.urls')),
     url(r'^api/recipe/', include('reciepe.urls', namespace='recipe')),
      url(r'^api/user/', include('userprofile.urls', namespace='userprofile')),
    url(r'^feed/', include('feed.urls')),
   url(r'^story/', include('story.urls')),
url(r'^music/', include('music.urls')),
url(r'^recipevideo/', include('recipevideo.urls')),

url(r'^polls/', include('polls.urls')),
url(r'^ingredient/', include('ingredient.urls')),

url(r'^comet/', include('mycometchatter.urls')),

url(r'^food/', include('myfood.urls')),
   url(r'^', include('food1.urls')),


]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
