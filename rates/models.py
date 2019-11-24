from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from pyuploadcare.dj.models import ImageField
from phone_field import PhoneField



#User Profile Model
class Profile(models.Model):
    prof_pic = ImageField(blank=True, manual_crop="")
    bio = models.CharField(max_length = 250)
    contact = PhoneField(blank=True, help_text='Contact phone number')
    user = models.OneToOneField('auth.User',on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.user)
    
    def save_profile(self):
        self.save()
        
        
    @classmethod    
    def update_bio(cls,id,new_bio):
        cls.objects.filter(pk = id ).update(bio = new_bio)
        new_bio_object = cls.objects.get(bio=new_bio)
        new_bio = new_bio_object.bio
        return new_bio

@receiver(post_save,sender=User)
def create_profile(sender, instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
    
@receiver(post_save,sender=User)
def save_profile(sender, instance,**kwargs):
    instance.profile.save()

    
    
#Project Model
class Project(models.Model):
    title = models.CharField(max_length = 50)
    project_pic = ImageField(blank=True, manual_crop="")
    description = models.CharField(max_length = 250)
    website= models.URLField(max_length=250)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def save_project(self):
            self.save()
        
    def __str__(self):
        return str(self.title)


    