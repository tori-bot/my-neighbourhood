

import logging
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Neighborhood,Business, Posts, User,Profile
from .forms import BusinessForm, PostForm, ProfileForm,NeighborhoodForm
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    
    
    return render(request,'home.html')

def profile_form(request, id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user=user)
    profile_form = ProfileForm()
    if request.method == 'POST':
        profile_form = ProfileForm(
            request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile_form.save()

            return redirect('profile')
        else:
            return HttpResponse('Please fill the form correctly.')
    else:
        context = {
            'profile_form': profile_form,
            'user': user,
            'profile': profile
        }
        return render(request, 'profile_form.html', context)

def profile(request):
    current_user = request.user
    user = User.objects.get(id=current_user.id)
    profile = Profile.get_profile_by_id(user.id)
    # neighborhood=Neighborhood.objects.all()
    neighborhood=Neighborhood.objects.filter(admin=current_user.id).first()
    business=Business.objects.filter(user_id=current_user.id)

    context = {
        'profile': profile,
        'user': user,
        'neighborhood':neighborhood,
        'business': business
        
    }
    return render(request, 'profile.html', context)

def user_profile(request, id):
    current_user = request.user
    user = User.objects.get(id=current_user.id)
    current_profile = Profile.get_profile_by_id(user.id)
    selected = get_object_or_404(User, id= id)
    print({selected})

    if selected == user:
        return redirect('home')
    
    profile=Profile.get_profile_by_id(selected.id)
    business=Business.objects.filter(user=selected.id)

    # projects=Project.objects.filter(user=selected.id)

    context = {
        'profile': profile,
        'business': business,
        'user': user,
        'current_profile': current_profile

    }
    return render(request, 'user_profile.html', context)

    # neighborhood views
def neighborhood_form(request):
    current_user= request.user
    # user = User.objects.get(id=id)
    # profile = Profile.objects.get(user=user)

    form = NeighborhoodForm()
    if request.method == 'POST':
        form = NeighborhoodForm(
            request.POST,request.FILES)
        if form.is_valid():
            new=form.save(commit=False)
            new.admin=current_user.profile
            new.save()

            return redirect('dashboard')
        else:
            return HttpResponse('Please fill the form correctly.')
    else:
        context = {
            'form': form,
            
        }
        return render(request, 'neighborhood_form.html', context)

def neighborhood(request,id):
    neighborhood= Neighborhood.objects.get(id=id)
    posts=Posts.objects.all().order_by('-published')
    # print(neighborhood)
    # posts=Posts.objects.filter(neighborhood=neighborhood)
    # print(posts)

    # current_user=request.user            
    # user = User.objects.get(id=id)
    # profile = Profile.objects.get(user=user)
    # hoods=Neighborhood.objects.all()
    # if hoods.count()<=0:
    #     return redirect('home')
    # else:
        
    #     neighborhood=Neighborhood.objects.filter(admin=current_user.id).first()
    #     print({neighborhood})
    #     posts=Posts.objects.all().order_by('-published')
        # posts=Posts.objects.filter(neighborhood=neighborhood.user).order_by('-published')
    
        
    context = {
        # 'user': user,
        # 'profile': profile,
        'neighborhood': neighborhood,
        'posts': posts
    }
    return render(request, 'neighborhood.html', context)

# business

def business_form(request):
    current_user= request.user
    
    form = BusinessForm()
    if request.method == 'POST':
        form = BusinessForm(
            request.POST, request.FILES)
        if form.is_valid():
            new=form.save(commit=False)
            new.user=current_user
            new.save()

            return redirect('home')
        else:
            return HttpResponse('Please fill the form correctly.')
    else:
        context = {
            'form': form,
            
        }
        return render(request, 'business_form.html', context)

def business(request,id):
    current_user=request.user
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user=user)
    neighborhood=Neighborhood.objects.filter(admin=current_user.id).first()
    business=Business.objects.all()
    # business=Business.objects.filter(neighborhood=neighborhood)
    context = {
        'user': user,
        'profile': profile,
        'business': business,
        'neighborhood': neighborhood
    }
    return render(request, 'business.html', context)

def search(request):
    current_user= request.user
    user = User.objects.get(id=current_user.id)
    profile = Profile.get_profile_by_id(user.id)
    if 'search' in request.GET and request.GET["search"]:
        search_term = request.GET.get("search")
        print(f'\n {search_term} \n')
        searched_business = Business.search_business(search_term)
        print(f'\n {searched_business} \n')
        message = f"{search_term}"    
    else:
        message = "Take this chance to search for a business in your neighborhood"

    context={
        'message': message,
        'business': searched_business,
        'user': user,
        'profile': profile
        }
    return render(request, 'searchit.html',context)

# posts
def post_form(request,id):
    current_user= request.user
    # neighborhood=Neighborhood.objects.get(id=id)
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            new=form.save(commit=False)
            new.user=current_user
            # new.neighborhood=neighborhood
            new.save()
            

            return redirect('home')
        else:
            return HttpResponse('Please fill the form correctly.')
    else:
        context = {
            'form': form,
            # 'user': user,
            # 'profile': profile
        }
        return render(request, 'post_form.html', context)

def join_neighborhood(request,id):
    neighborhood = Neighborhood.objects.get(id=id)
    request.user.profile.hood = neighborhood
    request.user.profile.save()
    print(request.user.profile.hood.name)
    return redirect('dashboard')

def leave_neighborhood(request,id):
    neighborhood = get_object_or_404(Neighborhood,id=id)
    request.user.profile.neighborhood = None
    request.user.profile.save()
    return redirect('dashboard')

def dashboard(request):
    
    neighborhoods=Neighborhood.objects.all()

    return render(request,'dashboard.html',{'neighborhoods':neighborhoods})

