from django.db import models

# Create your models here.
class Member(models.Model):
    username = models.CharField(max_length=100)
    description = models.TextField(blank=True,null=True)
    pic_profle =   models.ImageField(upload_to='profile/',null=True) 
    def __str__(self):
        return self.username.capitalize()