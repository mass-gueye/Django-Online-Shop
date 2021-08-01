from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class User(AbstractUser):
    phone_number = PhoneNumberField(unique = True, null = False, blank = False)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('login')