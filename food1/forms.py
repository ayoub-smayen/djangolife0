from django.forms import ModelForm
from .models import  NewSletter


class ContactForm(ModelForm):
    class Meta:
        model = NewSletter
        fields = '__all__'