from django.shortcuts import render,get_object_or_404
from .forms import ContactForm
# Create your views here.

from myfood.models import FoodPost, FoodPostImage


def index(request):
    posts = FoodPost.objects.all()
    return render(request, 'food1/index.html', {'posts': posts})


def detail_view(request, id):
    post = get_object_or_404(FoodPost, id=id)
    photos = FoodPostImage.objects.filter(foodpost=post)
    return render(request, 'food1/recipe-post.html', {
        'post': post,
        'photos': photos
    })


def index2(request):

    return render(request,"food1/contact.html")






def contact_view(request):
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact/contact.html', context)



