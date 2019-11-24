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