from django import forms
from django.db import models
from .models import Business,Post
from django.contrib.auth.models import User

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['name', 'email','description'] 

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'post']         