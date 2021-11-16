from django.contrib import messages

from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

# Create your views here.
def register(request):
    if request.method=="POST":
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'user name is already exist')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email is already registered')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1,first_name=firstname,last_name=lastname,email=email)
                user.save()
                print("user created")

        else:
            messages.info(request,'password incorrect')
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'registration.html')
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid details')
            return redirect('login')
    else:
        return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect('/')

