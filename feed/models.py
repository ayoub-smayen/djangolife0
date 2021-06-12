from django.db import models
from uuid import UUID
from math import  pi
import  random
# Create your models here.
from django.utils import timezone
from django.conf import settings
class Feed(models.Model):
    title = models.CharField(max_length= 112)
    content = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL ,on_delete = models.CASCADE)
    p_date = models.DateTimeField( editable=False ,null = True)
    u_date = models.DateTimeField( null  = True)
    image_feed = models.ImageField(upload_to="feed/images", blank=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.p_date = timezone.now()
        self.u_date = timezone.now()
        return super(Feed, self).save(*args, **kwargs)





# Create your models here.
class FeedComment(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL ,on_delete = models.CASCADE,related_name='feedcomments')
    feed = models.ForeignKey(Feed ,on_delete = models.CASCADE ,related_name='feedcomments')
    content = models.TextField()
    p_date = models.DateTimeField(editable=False ,null = True)
    u_date = models.DateTimeField(null = True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.p_date = timezone.now()
        self.u_date = timezone.now()
        return super(FeedComment, self).save(*args, **kwargs)


class FeedLike(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL ,on_delete = models.CASCADE,related_name='feedlikes')
    feed = models.ForeignKey( Feed ,on_delete = models.CASCADE ,related_name='feedlikes' )
    like = models.BooleanField()