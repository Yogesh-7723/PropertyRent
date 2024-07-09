# your_app/forms.py
from django import forms

from django.contrib.auth.models import User

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','is_staff','password']

