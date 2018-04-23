from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    # info about user
    class Meta:
        # base model
        model = User
        fields = ['username','email','password']
