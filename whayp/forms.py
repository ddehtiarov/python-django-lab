from django import forms
from django.contrib.auth.models import User

from .models import Post, Photo


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['description']


class PhotoForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ['photo_file']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']
