from django.conf import settings
from django.db import models
import  datetime
import  random
import  uuid
# Create your models here.
class Poststory(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='poststory', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField()
    story_date = models.DateTimeField(auto_now=True)
    image = models.FileField(blank=True,upload_to=f"storyies/{uuid.UUID.hex}/{datetime.datetime.now}/{random.choice([0,1,2,2])}")

    def __str__(self):
        return self.title


class PostImage(models.Model):
    post = models.ForeignKey(Poststory, default=None,related_name="postimages", on_delete=models.CASCADE)
    images = models.FileField(upload_to=f'images/{uuid.UUID.hex}')

    def __str__(self):
        return self.post.title