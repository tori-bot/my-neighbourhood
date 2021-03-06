from django.db import models


from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class Neighborhood(models.Model):
    name = models.CharField(max_length=50)
    landmark=models.ImageField(upload_to='landmarks/',null=True, blank=True)
    location=models.CharField(max_length=50,null=True)
    # user=models.OneToOneField(User,on_delete=models.CASCADE,null=True,related_name='neighbors')
    admin=models.ForeignKey('Profile',on_delete=models.CASCADE,null=True)
    occupants=models.IntegerField(default=0)
    

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

class Business(models.Model):
    name=models.CharField(max_length=50)
    picture=models.ImageField(upload_to='businesspics/',null=True, blank=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    neighborhood=models.ForeignKey(Neighborhood, on_delete=models.CASCADE,blank=True,null=True)
    email=models.EmailField(max_length=100)

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    # @classmethod
    # def find_business(cls,business_id):
    #     business=Business.objects.filter(id=business_id).first()
    #     return business

    @classmethod
    def get_business(cls,id):
        business = Business.objects.filter(user__id = id).first()
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
    hood=models.ForeignKey(Neighborhood,on_delete=models.CASCADE,null=True)
    
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

class Posts(models.Model):
    user=models.ForeignKey(User, related_name="posts",on_delete=models.CASCADE,null=True)
    neighborhood=models.ForeignKey(Neighborhood, related_name="neighbor_posts", on_delete=models.CASCADE,null=True,blank=True)
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='post_images/')
    post=models.TextField(null=True, blank=True)
    published=models.DateTimeField(auto_now_add=True)


    def create_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    def save_post(self):
        self.user

    @classmethod
    def get_posts(cls,neighborhood):
        posts = Posts.objects.filter(neighborhood=neighborhood)
        return posts


    def __str__(self):
        return self.title

# class Admin(models.Model):
#     name = models.CharField(max_length=100,null=True)
#     email=models.EmailField(max_length=50,null=True)
#     hood=models.OneToOneField(Neighborhood,on_delete=models.CASCADE,null=True)

#     def __str__(self):
#         return self.name
    