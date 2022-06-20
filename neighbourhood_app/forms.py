from django import forms
from .models import Profile,Business,Neighborhood

# class SignupForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput())
#     class Meta:
#         model = User
#         fields = ('name','neighborhood','email','profile_picture','password')

# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('email','password')

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ('name','user','neighborhood','email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_picture')

