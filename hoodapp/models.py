from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


class Neighbour(models.Model):
    name = models.CharField(max_length=150)

class Profile(models.Model):
    '''
    this is a class that defines the profile structure of our user
    '''
    user = models.OneToOneField(User,on_delete = models.CASCADE)    
    profile_pic = models.ImageField(upload_to= 'images/', default= 'default.jpg')
    bio = HTMLField()
    neighbourhood = models.CharField(max_length=200)
    
    

    
    

