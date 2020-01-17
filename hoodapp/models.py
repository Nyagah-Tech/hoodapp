from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Profile(models.Model):
    '''
    this is a class that defines the profile structure of our user
    '''
    user = models.OneToOneField(User,on_delete = models.CASCADE)    
    profile_pic = models.ImageField(upload_to= 'images/', default= 'default.jpg')
    bio = HTMLField()
    neighbourhood = models.CharField(max_length=200)
    
    def __str__(self):
        return self.user.username

class Business(models.Model):
    '''
    this class gives a blueprint how our bussinesses will be made
    '''
    posted_by = models.ForeignKey(User,on_delete = models.CASCADE)
    neighbourhood = models.CharField(max_length=100)
    email = models.EmailField()
    name = models.CharField(max_length=250)
    description = HTMLField()
    
    def __str__(self):
        return self.name
    
class Health(models.Model):
    '''
    this is a class blueprint or skeleton of how our health sectors will be stored
    '''
    neighbourhood = models.CharField(max_length=250)
    email =  models.EmailField()
    phone = models.IntegerField()
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    
class Police(models.Model)    :
    '''
    this describes the information that will be collected about the police stations
    '''
    name = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.IntegerField()
    neighbourhood = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name

    
class Post(models.Model):
    '''
    this creates the blueprint on which the post will rely on
    '''
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to= 'post/',blank=True)
    description = HTMLField()
    posted_by = models.ForeignKey(User,on_delete= models.CASCADE)
    posted_on = models.DateTimeField(auto_now_add=True)
    neighbourhood = models.CharField(max_length= 100)
    
    def __str__(self):
        return self.title