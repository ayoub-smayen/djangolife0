from django.db import models

# Create your models here.
class ingredientItem(models.Model):
  name = models.TextField()
  property = models.TextField()
  img_url = models.TextField()

class recipeItem(models.Model):
  name = models.TextField()
  ingredients = models.TextField()
  directions = models.TextField()
  img_url = models.TextField()
  list_ingredient = models.ManyToManyField(ingredientItem)