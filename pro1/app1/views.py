from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.models import User
import time
from django.contrib.auth.hashers import make_password
from .models import *


# Create your views here.
def base(request):
    return render(request,'base.html')

def index(request):
    if request.method =='POST':
        search_term = request.POST['location']
        articles = Property.objects.all().filter(address__icontains=search_term) 
    else:
        articles = Property.objects.all()
    return render(request,'home.html',{'articles':articles})
    

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def view_pro(request):
    return render(request,'view_property.html')

def user_login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST.get('password')
        user = User.objects.get(username=username)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request," login successfully !")
            return redirect('/')  
        else:       
            messages.warning(request,'user {user} not exists')
            return render(request,'login.html')
    else:       
        return render(request,'login.html')

def user_logout(request):
    logout(request)
    return redirect('/')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pass1 = make_password(request.POST['password'])
        # pass2 = request.POST['password2']
        print(email,username,pass1)
        print("come here your code ")
        obj = User.objects.all()
        print(obj)
        if User.objects.create(username=username,email=email,password=pass1):
            print("Successfully register ")
            return HttpResponseRedirect('/user_login/')
        else:
            fm = UserCreationForm()
            print("error")
            return render(request,'register.html',{'form':fm})
    else:
        fm = UserCreationForm()
        return render(request,'register.html')

def house(request):
    articles = Property.objects.filter(type__icontains='House')
    return render(request,'house.html',{'articles':articles})