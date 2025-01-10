from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import UserProfile, Company
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, "home.html")

def signup (request):
    if request.method == "GET":
        return render(request, "signup.html", {"form":UserCreationForm})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            # registrar usuario
            try:
                user= User.objects.create_user(username=request.POST["username"], password=request.POST["password1"])
                user.save()

                login(request, user)
                return redirect("companies", userN=user)
            except Exception as e:
                 return render(request, "signup.html", {"form":UserCreationForm,"error":"user already exist"})        
        return render(request, "signup.html", {"form":UserCreationForm,"error":"Password do not match"})

@login_required
def companies (request, userN):
    if request.method == "GET":
        companies = Company.objects.all()
        return render(request, "companies.html", {"companies":companies})
    else:
        user = User.objects.get(username=userN)           
        company = Company.objects.get(nombre=request.POST["company"])
        userProfile = UserProfile(user=user,company=company)
        userProfile.save()
        return redirect("/projects")

@login_required
def signout(request):
    logout(request)
    return redirect("home")

def signin(request):

    if request.method == "GET":
        return render(request, "signin.html", {"form":AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is None:
            return render(request, "signin.html", {"form":AuthenticationForm, "error":"Username or Password is incorrect"})
        else:
            login(request, user)
            return redirect("/projects")