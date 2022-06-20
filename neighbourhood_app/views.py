
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import User,Profile
from .forms import ProfileForm




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

            return redirect('home')
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
    # projects=Project.objects.filter(user=user.id).order_by('-published')

    context = {
        'profile': profile,
        'user': user,
        
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