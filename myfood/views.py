from django.shortcuts import render,get_object_or_404
# Create your views here.
from .models import FoodPost, FoodPostImage


def blog_view(request):
    posts = FoodPost.objects.all()
    return render(request, 'food/blog.html', {'posts': posts})


def detail_view(request, id):
    post = get_object_or_404(FoodPost, id=id)
    photos = FoodPostImage.objects.filter(foodpost=post)
    return render(request, 'food/detail.html', {
        'post': post,
        'photos': photos
    })

def chatter(request):
    return  render(request,"food/chatter.html")
