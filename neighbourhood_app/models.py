from django.db import models

from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from datetime import date

from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Admin(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=300)
    neighborhood_admin = models.CharField(max_length=300,null=True)

    def __str__(self):
        return self.name

class Neighborhood(models.Model):
    name = models.CharField(max_length=50)
    location=models.CharField(max_length=50,null=True)
    occupants=models.IntegerField()
    admin=models.ForeignKey(Admin,on_delete=models.CASCADE)

    def create_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()

    @classmethod
    def find_neighbourhood(cls,neighborhood_id):
        neighborhood=Neighborhood.objects.filter(id=neighborhood_id).first()
        return neighborhood

    def update_neighborhood(self,name,location,occupants,admin):
        self.name=name
        self.location=location
        self.occupants=occupants
        self.admin=admin
        self.save()

    def update_occupants(self,occupants,add_occupant):
        self.occupants=occupants+add_occupant
        self.save()

    def __str__(self):
        return self.name
class User(AbstractUser):
    name=models.CharField(max_length=50,null=True)
    neighborhood=models.ForeignKey(Neighborhood,on_delete=models.CASCADE,related_name='users',null=True)
    email=models.EmailField(max_length=300,null=True)
    password=models.CharField(max_length=200,null=True)
    profile_picture=models.ImageField(upload_to='profilepics/',null=True)

    def __str__(self):
        return self.name

class Business(models.Model):
    name=models.CharField(max_length=50)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    neighborhood=models.ForeignKey(Neighborhood, on_delete=models.CASCADE)
    email=models.EmailField(max_length=100)

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def find_business(cls,business_id):
        business=Business.objects.filter(id=business_id).first()
        return business

    def update_business(self,name,user,neighborhood,email):
        self.name=name
        self.user=user
        self.neighborhood=neighborhood
        self.email=email
        self.save()

    @classmethod
    def search_business(cls,search_term):
        business=cls.objects.filter(name__icontains=search_term).all()
        return business

    def __str__(self):
        return self.name

class Profile(models.Model):
    user=models.OneToOneField(User,primary_key=True,on_delete=models.CASCADE)   
    profile_picture=models.ImageField(upload_to='profile_pictures/',default='default.jpg',null=True) 
    bio=models.TextField()
    
    @receiver(post_save, sender=User) 
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)


    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()

    def delete_profile(self):
        self.delete()

    def update_profile(self,user,profile_picture,bio):
        self.user=user
        self.profile_picture=profile_picture
        self.bio=bio
        self.save()

    @classmethod
    def get_profile_by_id(cls,id):
        profile = Profile.objects.filter(user__id = id).first()
        return profile

    @classmethod
    def search_profile(cls,search_term):
        profile=cls.objects.filter(user__username__icontains=search_term).all()
        return profile

    def __str__(self):
        return self.user