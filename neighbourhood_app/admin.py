from django.contrib import admin
from .models import User,Profile,Neighborhood,Business,Admin
# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Business)
admin.site.register(Neighborhood)
admin.site.register(Admin)