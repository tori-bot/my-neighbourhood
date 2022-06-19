from django.db import models

from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from datetime import date


# Create your models here.
class Admin(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)

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


class User(AbstractUser):
    name=models.CharField(max_length=50,null=True)
    neighborhood=models.ForeignKey(Neighborhood,on_delete=models.CASCADE,related_name='users',null=True)
    email=models.EmailField(max_length=100,null=True)

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