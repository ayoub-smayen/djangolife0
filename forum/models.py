from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField

from decimal import Decimal
from  string import  ascii_letters


d  = [i for i  in  ascii_letters]
from datetime import  datetime

v = datetime.date(datetime.now())
import  random

random.seed()

g=random.choice(d)
# Create your models here.


class Posts(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    comment = ArrayField(models.CharField(max_length=50), default=[])
    postimg = models.ImageField(upload_to=f"posts/{g}/p")
    postfile = models.ImageField(upload_to=f"posts/{v}/doct/{g}/v/")
    posttitle = models.CharField(max_length=30, default='')
    potBody = models.TextField()

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts', on_delete=models.CASCADE)
    def __str__(self):
        return self.id +  " " + self.comment

    class Meta:
        db_table="posts"



class Comments(models.Model):
    commentbody = models.TextField()
    name = models.CharField(max_length=50)
    commenttag = models.CharField(max_length=150)
    #post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comments',null=True)
    rating = models.PositiveSmallIntegerField(default=0)
    likes = models.PositiveSmallIntegerField(default=0)
    commentdate= models.DateTimeField(auto_now_add=True)
    description = models.TextField(default='Product description.')
    file_comment=models.FileField(upload_to=f"comments/{v}/docs/{g}")
    image_url = models.ImageField(upload_to=f"comments/{v}/c0/")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='comments', on_delete=models.CASCADE)
    def __str__(self):
        return self.id
    class Meta:
        db_table = 'comments'

