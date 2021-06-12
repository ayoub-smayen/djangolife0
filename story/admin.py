from django.contrib import admin

# Register your models here.
from .models import Poststory, PostImage


class PostImageAdmin(admin.StackedInline):
    model = PostImage


@admin.register(Poststory)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
        model = Poststory


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass