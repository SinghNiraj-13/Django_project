from django.db import models
from django.contrib.auth.models import User
from localflavor.in_.models import INStateField
#from localflavor.in_.forms import INZipCodeField
# Create your models here.

class Location(models.Model):
    Address_line_1 = models.CharField(max_length= 170)
    Address_line_2 = models.CharField(max_length=170, null=True)
    City = models.CharField(max_length=64)
    State = INStateField(default='WB')
    #Pincode = INZipCodeField(blank=True)

    def __str__(self):
        return f'Location {self.id}'

class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    photo= models.ImageField(null=True)
    bio= models.CharField(max_length=140, blank=True)
    phone_number= models.CharField(max_length=12, blank=True)
    location =models.OneToOneField(Location, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.user.username}\'s Profile'

