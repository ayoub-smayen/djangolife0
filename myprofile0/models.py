from django.core.validators import MinLengthValidator
from django.db import models
from django.conf import settings
#from   django.contrib.auth.models import  User
import  random
import  string
import uuid
from datetime import datetime
from  api.models import  User
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

letters = [s for s in string.ascii_letters]

ch = random.seed(0)
l = random.choice(letters)


class UserProfileManager(models.Manager):
    pass
# Create your models here.
class Myprofile(models.Model):
    GENDER = (
        ('M', 'Homme'),
        ('F', 'Femme'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="myprofile",on_delete=models.CASCADE)
    first_name = models.CharField(max_length=120, blank=False)
    last_name = models.CharField(max_length=120, blank=False)
    gender = models.CharField(max_length=1, choices=GENDER)
    zip_code = models.CharField(max_length=5, validators=[MinLengthValidator(5)],blank=False)
    image_pic = models.ImageField(upload_to=f"users/{current_time}/{l}/c0/{str(uuid.uuid4())}/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return f'profile of  {self.user.email}'

    def save(self, *args, **kwargs):

        return super(Myprofile, self).save(*args, **kwargs)  #

    @receiver(post_save, sender=User)
    def create_profile_for_user(sender, instance=None, created=False, **kargs):
        if created:
            Myprofile.objects.get_or_create(user=instance)

    @receiver(pre_delete, sender=User)
    def delete_profile_for_user(sender, instance=None, **kargs):
        if instance:
            user_profile = Myprofile.objects.get(user=instance)
            user_profile.delete()
def createProfile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Myprofile.objects.created(user=kwargs['instance'])

        post_save.connect(createProfile, sender=User)