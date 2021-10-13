from django.db import models

# Create your models here.
class UserModels(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=30)