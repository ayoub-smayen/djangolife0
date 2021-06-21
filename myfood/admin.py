from django.contrib import admin

# Register your models here.
from .models import FoodPost, FoodPostImage


class PostImageAdmin(admin.StackedInline):
    model = FoodPostImage


@admin.register(FoodPost)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
        model = FoodPost


@admin.register(FoodPostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass