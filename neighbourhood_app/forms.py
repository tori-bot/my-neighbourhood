from django import forms
from .models import Profile, User

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name','neighbourhood','email','password')

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email','password')