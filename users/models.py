from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    image= models.ImageField(upload_to='profile/', blank=True, default= 'profile/default.jpg')
