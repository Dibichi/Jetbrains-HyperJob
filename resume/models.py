# Create your models here
from django.db import models
import django
from django.contrib.auth.models import User

# Create your models here.

# Business object that stores all data regarding the creator and description of the resume
class Resume(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=1024)
