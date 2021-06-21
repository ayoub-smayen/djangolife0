from django.db import models
from datetime import datetime
# Create your models here.
import random
class FoodPost(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    ingredients = models.TextField()
    image = models.FileField(upload_to=f"food/{random.choice([i for  i in range(100)])}/{str(datetime.now())[:4]}",blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class FoodPostImage(models.Model):
    foodpost = models.ForeignKey(FoodPost,related_name='foodpost', default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to=f'foodposts/{str(datetime.now())[:4]}/images/{random.choice([i for i in range(100)])}')


    #def __str__(self):
    #    return "foodpost"


    def __str__(self):
        return self.foodpost.title