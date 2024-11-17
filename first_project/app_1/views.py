from django.shortcuts import render
from django.http import HttpResponse
from .forms import user_sign_up
from django.http import HttpResponseRedirect
from .forms import user_login
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login



# Create your views here

# we are validate the form data from the user input
def sign_up(request):
    stu=user_sign_up
    if request.method == 'POST':
        stu=user_sign_up(request.POST)
        if stu.is_valid():
            name=stu.cleaned_data['username']
            email= stu.cleaned_data['email']
            password=stu.cleaned_data['password']
            user = User.objects.create_user(username=name, email=email, password=password)
            user.save()
            return HttpResponseRedirect('/login')
    else:
        stu=user_sign_up
    return render(request, 'sign_in.html',{'st':stu})




# we are render foam data in the login foam and authenticate and login the user
def log_in(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/home')  # Redirect to the home page after login
        else:
            return HttpResponse('Invalid username or password')
    else:
        sk=user_login
    return render(request, 'login.html',{'login':sk})



# we are create a simple home page 
def home(request):
    return render(request,'home.html')
