from django.contrib import admin

# Register your models here.
from .models import recipeItem ,ingredientItem

admin.site.register(recipeItem)
admin.site.register(ingredientItem)
