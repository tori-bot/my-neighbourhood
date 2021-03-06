from django import forms
from .models import Posts, Profile,Business,Neighborhood

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ('name','user','neighborhood','email')
 
class NeighborhoodForm(forms.ModelForm):
    class Meta:
        model=Neighborhood
        fields = ('name','landmark','location')

class BusinessForm(forms.ModelForm):
    class Meta:
        model=Business
        fields = ('name','picture','email')
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_picture')

class PostForm(forms.ModelForm):
    class Meta:
        model=Posts
        fields = ('title','image','post')