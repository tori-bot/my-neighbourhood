
from django.http import HttpResponse
from django.shortcuts import redirect, render




# Create your views here.
def home(request):
    return render(request,'home.html')

# def signup(request):
#     form = SignupForm()
#     if request.method == 'POST':
#         form = SignupForm(
#             request.POST, request.FILES)
#         print(request.POST.get('password'))
#         if form.is_valid():
#             form.save()
#             # name=form.cleaned_data.get('name')
#             # neighborhood=form.cleaned_data.get('neighborhood')
#             # email=form.cleaned_data.get('email')
#             # password=form.cleaned_data.get('password')
#             # user = authenticate(name=name,email=email, neighborhood=neighborhood,password=password)
#             # login(request,user)

#             return redirect('home')
#         else:
#             return HttpResponse('Please fill the form correctly.')
#     else:
#         context = {
#             'form': form,
#         }
#     return render(request,'django_registration/registration_form.html',context)

# def login(request):
#     form = LoginForm()
#     if request.method == 'POST':
#         form = LoginForm(
#             request.POST)
#         if form.is_valid():
#             form.save()

#             return redirect('home')
#         else:
#             return HttpResponse('Please fill the form correctly.')
#     else:
#         context = {
#             'form': form,
#         }
#     return render(request,'registration/login.html',context)