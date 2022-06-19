from django import forms
from .models import Profile, User

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('name','neighborhood','email')

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email','password')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_picture')