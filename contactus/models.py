from django.db import models

# Create your models here.
class ContactUs(models.Model):
    username = models.CharField(max_length=120)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=8)
    message = models.TextField()

    def _str_(self):
        return self.username
