#from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# from PIL import Image
from string import ascii_letters
import random
from datetime import datetime

d = datetime.date(datetime.now())

fg = f"{d}".join(random.choice([j for j in ascii_letters]))


def upload_path(instance, filename):
    return '/'.join(['picturesandvideos', str(instance.title), filename])


class RecipeVideo(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='recipesvideo', on_delete=models.CASCADE)
    # author = models.ForeignKey(User, related_name="recipes",  on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    cooktime = models.TextField()
    ingredients = models.TextField()
    directions = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    picture = models.ImageField(blank=True, null=True, upload_to=f"reciepevideos/{fg}/")
    video = models.FileField(blank=True, null=True, upload_to=f"recipesvideosusers/{fg}/")

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title