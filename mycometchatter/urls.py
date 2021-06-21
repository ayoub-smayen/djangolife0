from django.urls import path

from .views import band_listing,band_listing2

urlpatterns = [
    path('', band_listing, name='band-list'),
path('websql/', band_listing2, name='band-list2'),
    #path('bands/<int:band_id>/', views.band_detail, name='band-detail'),
    #path('bands/search/', views.band_search, name='band-search'),
]