from django import forms
from .models import BillingAddress



class BillingForm(forms.ModelForm):
    class Meta:
        model = BillingAddress
        fields = ['phone_number','address', 'zipcode', 'city', 'country']