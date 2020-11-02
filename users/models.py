from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):

    """ Custom User Model"""

    photo = models.ImageField(upload_to="user_photos", blank=True)
    admin = models.BooleanField(default=False)
