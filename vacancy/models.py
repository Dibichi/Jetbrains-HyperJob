from django.db import models
import django
from django.contrib.auth.models import User

# Business object that stores all data regarding the creator description of the vacancy
class Vacancy(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=1024)
