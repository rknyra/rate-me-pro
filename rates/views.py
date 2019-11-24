from django.shortcuts import render
from django.contrib.auth.decorators import login_required


#VIEWS

#index
def index(request):
      
    return render(request, 'index.html', locals())



#profilePage
def myProfile(request):
      
    return render(request, 'rmp_pages/profile.html', locals())


#submitProject
@login_required(login_url='/accounts/login')
def submitProject(request):
      
    return render(request, 'rmp_pages/submit_project.html', locals())