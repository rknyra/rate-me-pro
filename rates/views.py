from django.shortcuts import render


#VIEWS

#index
def index(request):
      
    return render(request, 'index.html', locals())



#profilePage
def myProfile(request):
      
    return render(request, 'rmp_pages/profile.html', locals())


#submitProject
def submitProject(request):
      
    return render(request, 'rmp_pages/submit_project.html', locals())