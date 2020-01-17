from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .email import send_register_confirm_email
from django.contrib.auth.decorators import login_required
from .forms import *


# Create your views here.

def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password1 == password:
            if User.objects.filter(username=username):
                messages.info(request, 'This Username is taken!')
                return redirect('registration')
            elif User.objects.filter(email=email):
                messages.info(request, 'This Email is taken!')
                return redirect('registration')
            else:
                user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)   
                user.save()           
                
                return redirect('home')
        else:
            messages.info(request,'Passwords should match!')
            return redirect('registration')
    else:
        return render(request,'auth/registration.html')
    
@login_required
def home(request):
    '''
    renders our homepage
    '''
    return render(request,'all/home.html')
        
@login_required
def add_bussiness(request):
    '''
    this view function either renders our add bussiness form our saves a new bussiness
    '''
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        hood = request.POST.get('Location')
        if form.is_valid():
            bussiness = form.save(commit=False)
            bussiness.neighbourhood = hood
            bussiness.posted_by = request.user
            bussiness.save()
            return redirect('home')
        else:
            messages.info(request,"all fields are required")
            return redirect('add-bussiness')
    else:
        form = BusinessForm()
        return render(request,'all/add_bs.html',{"form":form})

@login_required
def new_post(request):
    '''
    this is a view function that renders our new post form aswell as save our new post in the db
    '''
    profile = Profile.objects.get(user = request.user)
    if profile.neighbourhood is None:
        messages.info(request,'Provide your neighbourhood information first!')
        return redirect('update-profile')
    else:
        if request.method == 'POST':
            form = PostForm(request.POST,request.FILES)
            if form.is_valid():
                post = form.save(commit = False)
                post.posted_by = request.user
                post.neighbourhood = profile.neighbourhood
                post.save()
                return redirect('home')
            else:
                messages.info(request,'All fields are required')
                return redirect('new-post')
        else:
            form = PostForm()
            return render(request,'all/new_post.html',{"form":form})
            
            
        
        
