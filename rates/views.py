from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.models import User
from .forms import UpdateProfileForm, SubmitProjectForm, RateProjectForm
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Avg

#VIEWS

#index
def index(request):
    
    projects=Project.objects.all()
    

    rateForm = RateProjectForm()
    return render(request, 'index.html', locals())

#rateProjects
@login_required(login_url='/accounts/login')
def rateProjects(request, project_id):
    # reviews/ratings
    project = get_object_or_404(Project,pk=project_id)
    reviews = Review.objects.filter(project = project)
    design = reviews.aggregate(Avg('design'))['design__avg']
    usability = reviews.aggregate(Avg('usability'))['usability__avg']
    content = reviews.aggregate(Avg('content'))['content__avg']
    average = reviews.aggregate(Avg('average'))['average__avg']
    
    if request.method == 'POST':
        rateForm = RateProjectForm(request.POST)
        if rateForm.is_valid():
            rates = rateForm.save(commit=False)
            rates.average = (rates.design + rates.usability + rates.content) / 3
            rates.project = project
            rates.user = request.user
            rates.save()
    
    return redirect('index')
        



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
            upload.user = request.user
            upload.save()
        
        return redirect('index')
    else:
        submitProjectForm = SubmitProjectForm()
        return render(request, 'rmp_pages/submit_project.html', locals())



#updateProfile
@login_required(login_url='/accounts/login')
def updateProfile(request):
    
    my_prof = Profile.objects.get(user=request.user)
        
    
    if request.method == 'POST':
        updateProf = UpdateProfileForm(request.POST,request.FILES,instance=request.user.profile)

        if updateProf.is_valid():
            updateProf.save()
            
            
        return redirect('my_profile')
    else:
        updateProf = UpdateProfileForm(instance=request.user.profile)
    
      
    return render(request, 'rmp_pages/update_profile.html', locals())



#search projects
def searchProjects(request):
    if 'search' in request.GET and request.GET["search"]:
    
        search_term = request.GET.get("search")
        searched_projects = Project.objects.filter(title__icontains=search_term)
        message = f"{search_term}" 
        
        return render(request, 'rmp_pages/search_results.html', locals())
      
    else:
        message = "you haven't searched for any project"  
    return render(request, 'rmp_pages/search_results.html', locals())
