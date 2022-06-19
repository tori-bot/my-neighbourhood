from django.shortcuts import render

from neighbourhood_app.forms import SignupForm

# Create your views here.
def home(request):
    return render(request,'home.html')

def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(
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
    return render(request,'signup.html',context)