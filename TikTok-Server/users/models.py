import os

from django.contrib.auth.models import AbstractUser
from django.db import models


# Function to get the path of the image and save in the specific path
def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.id, ext)
    return os.path.join('avatar/', filename)


# This models extend the default user model.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to=get_file_path, blank=True)
    description = models.CharField(max_length=100, blank=True)
    website = models.CharField(max_length=100, blank=True)
    instagram = models.CharField(max_length=100, blank=True)
    first_name = models.CharField(max_length=100, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    # Specific email to login in web, the default is a username.
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
