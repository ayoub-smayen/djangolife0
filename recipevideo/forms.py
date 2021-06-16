from django import forms
from .models import RecipeVideo

class RecipeForm(forms.ModelForm):
    class Meta:
        model = RecipeVideo
        fields = ('title',
                  'cooktime',
                  'ingredients',
                  'directions',
                  'video',
                  'picture')