from django.shortcuts import render


#VIEWS

#index
def index(request):
      
    return render(request, 'index.html', locals())