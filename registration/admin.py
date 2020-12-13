from django.contrib import admin
from .models import ProfileSettings


@admin.register(ProfileSettings)
class Admin(admin.ModelAdmin):
    list_display = ['id', 'birth_date', "profile_image"]

# Register your models here.
