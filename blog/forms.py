from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'author', 'body', 'photo']


class PostEditForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'body']
