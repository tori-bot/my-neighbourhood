from django import forms
from .models import Profile,Business,Neighborhood

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ('name','user','neighborhood','email')
 
class NeighborhoodForm(forms.ModelForm):
    class Meta:
        model=Neighborhood
        fields = ('name','location','occupants','user')
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_picture')

