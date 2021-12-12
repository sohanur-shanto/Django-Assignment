from django.contrib import admin
from . models import *

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'avatar', 'gender', 'number', 'address', 'birthday', 'phone', 'zip', 'created_at', 'updated_at']


