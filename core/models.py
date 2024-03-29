from django.contrib.auth.models import AbstractUser
from django.db import models
from  django.conf import settings
# Create your models here.
from django.utils.translation import ugettext_lazy as _

import  uuid

# class BaseModel(models.Model):
#     """Base model for the application. Uses UUID for pk."""
#     id = models.UUIDField(
#         primary_key=True,
#         editable=False,
#         default=uuid.uuid4,
#     )
#
#     class Meta:
#         """Metadata."""
#         abstract = True
#
#
# class User(BaseModel, AbstractUser):
#     """Custom user model."""
#     username = models.CharField(blank=True, null=True,max_length=255)
#     email = models.EmailField(_('email address'), unique=True)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
#
#     def __str__(self):
#         return "{}".format(self.email)
#
# class UserProfile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile0')
#     title = models.CharField(max_length=255)
#     dob = models.DateField()
#     address = models.CharField(max_length=255)
#     country = models.CharField(max_length=50)
#     city = models.CharField(max_length=50)
#     zip = models.CharField(max_length=5)
#     photo = models.ImageField(upload_to='uploads', blank=True)