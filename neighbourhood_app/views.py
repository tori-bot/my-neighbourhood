
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Neighborhood,Business, User,Profile
from .forms import BusinessForm, ProfileForm,NeighborhoodForm




# Create your views here.
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
    neighborhood=Neighborhood.objects.filter(id=current_user.id).first()
    business=Business.objects.filter(id=current_user.id)

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
    # projects=Project.objects.filter(user=selected.id)

    context = {
        'profile': profile,
        
        'user': user,
        'current_profile': current_profile

    }
    return render(request, 'user_profile.html', context)

    # neighborhood views
def neighborhood_form(request,id):
    current_user= request.user
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user=user)
    form = NeighborhoodForm()
    if request.method == 'POST':
        form = NeighborhoodForm(
            request.POST)
        if form.is_valid():
            form.save()

            return redirect('neighborhood')
        else:
            return HttpResponse('Please fill the form correctly.')
    else:
        context = {
            'form': form,
            'user': user,
            'profile': profile
        }
        return render(request, 'neighborhood_form.html', context)

def neighborhood(request,id):
    current_user=request.user            
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user=user)
    neighborhood=Neighborhood.objects.filter(id=user.id).first()
    context = {
        'user': user,
        'profile': profile,
        'neighborhood': neighborhood
    }
    return render(request, 'neighborhood.html', context)

# business

def business_form(request,id):
    current_user= request.user
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user=user)
    form = BusinessForm()
    if request.method == 'POST':
        form = BusinessForm(
            request.POST)
        if form.is_valid():
            form.save()

            return redirect('business')
        else:
            return HttpResponse('Please fill the form correctly.')
    else:
        context = {
            'form': form,
            'user': user,
            'profile': profile
        }
        return render(request, 'business_form.html', context)

def business(request,id):
    current_user=request.user
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user=user)
    neighborhood=Neighborhood.objects.get  (id=current_user.id)
    business=Business.objects.filter(neighborhood=neighborhood)
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