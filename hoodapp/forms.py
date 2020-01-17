from django.contrib.auth.models import User
from django import forms
from .models import Business

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = [
            'neighbourhood',
            'posted_by'
        ]