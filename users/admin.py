from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import UserModels
# Register your models h
@admin.register(UserModels)
class userAdmin(admin.ModelAdmin):
    list_display=['name','email','password']
