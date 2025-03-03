from django import forms
from .models import Country,City

class studentform(forms.ModelForm):
    class Meta:
        #imports model from model.py
        model = Country
        #__all__ includes all the fields from country model
        fields ='__all__'

class cityform(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'


#if wanted to add more models create its own class


