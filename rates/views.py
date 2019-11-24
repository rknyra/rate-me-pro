from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.models import User
from .forms import UpdateProfileForm, SubmitProjectForm
from django.core.exceptions import ObjectDoesNotExist


#VIEWS

#index
def index(request):
      
    return render(request, 'index.html', locals())



#profilePage
def myProfile(request):
    userProjects = Project.objects.filter(user=request.user)
    userProfile = Profile.objects.all()
      
    return render(request, 'rmp_pages/profile.html', locals())



#submitProject
@login_required(login_url='/accounts/login')
def submitProject(request):
      
    return render(request, 'rmp_pages/submit_project.html', locals())



#submitProject
@login_required(login_url='/accounts/login')
def updateProfile(request):
      
    return render(request, 'rmp_pages/update_profile.html', locals())