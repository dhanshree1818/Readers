from django.contrib.auth.models import User
from django.contrib.gis.geoip2.resources import Country
from django.db import models
from django.utils import timezone

# Create your models here.


class Register(User):
    Agree_Toc = models.BooleanField(blank=False,default=True)
    dob = models.DateField(null=False)
    recovery_email = models.CharField(max_length=100)

class Book:
    book_name=models.CharField(max_length=100)


