from django.db import models

# Create your models here.
from django.db import models
#from django.contrib.auth.models import User
from  api.models import User
# Create your models here.
class Profile(models.Model):
    email = models.EmailField()
    image = models.ImageField(upload_to="profile_img" ,blank = True)
    description = models.CharField(max_length = 112)
    user = models.OneToOneField(User , on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username