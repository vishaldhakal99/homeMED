from django.shortcuts import render,HttpResponse,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .models import userProfile
from home.views import index

def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        option = request.POST.get("category")
        
        if User.objects.filter(email = email).exists():
            return HttpResponse("Email Already Exists")
        else:
            user = User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name)
            prof = userProfile.objects.get(user=user)
            if(option == "patient"):
                prof.is_patient = True
            else:
                prof.is_doctor = True
            prof.save()
            user.save()
            return render(request,'accounts/register.html')

    return render(request,'accounts/register.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            return redirect('login')

    else:
        return render(request, 'accounts/register.html')

def logout(request):
    id = request.user.id
    usersobj = User.objects.get(pk=id)
    auth.logout(request)
    return redirect('register')