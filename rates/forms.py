from django import forms
from .models import Profile, Project, Review
from pyuploadcare.dj.forms import ImageField


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=['prof_pic','bio','contact']
        
        
class SubmitProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields=('title','project_pic','description', 'website')

class RateProjectForm(forms.ModelForm):
    class Meta:
        model = Review
        fields=('design','usability','content')