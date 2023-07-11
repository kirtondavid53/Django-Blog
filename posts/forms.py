from django.forms import ModelForm
from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ("date_created", "author", )

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'body' : forms.Textarea(attrs={'class': 'form-control'}),
            'snippet' : forms.TextInput(attrs={'class': 'form-control'}),
        }