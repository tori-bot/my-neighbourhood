from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),

    path('profile_form/<int:id>/', views.profile_form, name='profile_form'),
    path('profile/', views.profile, name='profile'),
    path('user_profile/<int:id>/',
         views.user_profile, name='user_profile'),
]