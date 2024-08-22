from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import login

def loginpage(request):
    return render (request,'loginpage.html')

def signuppage(request):
    return render (request,'signuppage.html')

def user_create(request):
    if request.method=='POST': 
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        username=request.POST['uname']
        password=request.POST['pass']
        cpassword=request.POST['cpass']
        email=request.POST['mail']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'This username already exists')
                return redirect('signuppage')
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password,email=email)
                user.save()
        else:
            messages.info(request,'Password doesnot match')
            return redirect('signuppage')
        return redirect('loginpage')
    else:
        return render(request,'signuppage.html')
    

def log(request):
    if request.method=='POST':
        username=request.POST['usname']
        password=request.POST['passd']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            if user.is_staff:
                print('ok')
                login(request,user)
                return redirect('adminmod')
            else:
                login(request,user)
                auth.login(request,user)
                return redirect('usermod')
        else:
            messages.info(request,'Invalid Username or Password')
            return redirect('loginpage')
    return render(request,'signuppage.html')

def adminmod(request):
    return render (request,'adminmod.html')

def usermod(request):
    return render (request,'usermod.html')

def lgout(request):
    auth.logout(request)
    return redirect ('signuppage')