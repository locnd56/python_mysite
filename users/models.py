from django.db import models
from django.contrib.auth.models import User,AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    """docstring for CustomUser"""
    date_of_birth = models.DateTimeField(max_length=50, null=True)
    def __str__(self):
        return self.email

