from django.contrib.auth.models import User
from django import forms
from .models import *

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = [
            'neighbourhood',
            'posted_by'
        ]
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = [
            'posted_by',
            'posted_on',
            'neighbourhood',
        ]