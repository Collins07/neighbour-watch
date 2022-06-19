from django import forms
from django.db import models
from .models import Business
from django.contrib.auth.models import User

class BusinessForm(forms.ModelForm):
    class Meta:
        model: Business
        fields = ['name', 'email','description', 'price'] 