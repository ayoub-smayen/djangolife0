from django.contrib import admin

# Register your models here.
#from django.contrib import admin
from .models import Friend, Favorite
from reciepe.models import Recipe

# Register your models here.
admin.site.register(Friend)
admin.site.register(Favorite)