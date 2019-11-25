from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.models import User
from .forms import UpdateProfileForm, SubmitProjectForm
from django.core.exceptions import ObjectDoesNotExist


#VIEWS

#index
def index(request):
    
    projects=Project.objects.all()
      
    return render(request, 'index.html', locals())



#profilePage
def myProfile(request):
    userProjects = Project.objects.filter(user=request.user)
    userProfile = Profile.objects.all()
      
    return render(request, 'rmp_pages/profile.html', locals())



#submitProject
@login_required(login_url='/accounts/login')
def submitProject(request):
        
    submitProjectForm = SubmitProjectForm()
    
    if request.method == 'POST':
        submitProjectForm = SubmitProjectForm(request.POST,request.FILES)
        user = request.user.id
        
        if submitProjectForm.is_valid():
            upload = submitProjectForm.save(commit=False)
            upload.user = request.user.profile
            upload.profile = request.user
            upload.save()
        
        return redirect('index')
    else:
        submitProjectForm = SubmitProjectForm()
        return render(request, 'rmp_pages/submit_project.html', locals())



#updateProfile
@login_required(login_url='/accounts/login')
def updateProfile(request):
    
    my_prof = Profile.objects.get(user=request.user)
    updateProf = UpdateProfileForm(instance=request.user)
    
    
    if request.method == 'POST':
        updateProf = UpdateProfileForm(request.POST,request.FILES,instance=request.user.profile)

        if updateProf.is_valid():
            updateProf.save()
            
            
        return redirect('my_profile')
    else:
        updateProf = UpdateProfileForm(instance=request.user.profile)
    
      
    return render(request, 'rmp_pages/update_profile.html', locals())