from django import forms
from django.db import models
from .models import Business,Post,UserProfile
from django.contrib.auth.models import User

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['name', 'email','description'] 

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'post']        

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture', 'location']


class UserForm(forms.ModelForm):
    email = forms.EmailField(max_length=300, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email')          