from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    GENDER_CHOICES = [('M','Male'),('F','Female')]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length= 30)
    phone_number = models.CharField(max_length = 15,blank=True,null=True)
    address = models.TextField(blank=True)
    gender = models.CharField(max_length=1,choices= GENDER_CHOICES,null=True,blank=True)
    
    def __str__(self):
        return self.user.username

 
 
 