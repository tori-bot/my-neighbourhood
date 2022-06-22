from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),

    path('profile_form/<int:id>/', views.profile_form, name='profile_form'),
    path('profile/', views.profile, name='profile'),
    path('user_profile/<int:id>/',
         views.user_profile, name='user_profile'),

    path('neighborhood_form/', views.neighborhood_form, name='neighborhood_form'),
    path('neighborhood/<int:id>/', views.neighborhood, name='neighborhood'),

    path('business_form/', views.business_form, name='business_form'),
    path('business/<int:id>/', views.business, name='business'),

    path('post_form/<int:id>/', views.post_form, name='post_form'),

    path('search/', views.search, name='search'),
    path('leave_neighborhood/<int:id>/', views.leave_neighborhood, name='leave_neighborhood'),
    path('join_neighborhood/<int:id>/', views.join_neighborhood, name='join_neighborhood'),

    path('dashboard/', views.dashboard, name='dashboard'),

]