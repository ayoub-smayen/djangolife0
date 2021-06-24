from django import forms
from .models import Profile

from api.models import User

from django.contrib.auth.forms import UserCreationForm


# forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username","email","password",)
