# from django.core import validators
from django import forms
from django.db.models import fields
from .models import ProfileSettings
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username",
                  "email", "password1", "password2", ]


class ProfileSettingsForm(forms.ModelForm):
    class Meta:
        model = ProfileSettings
        fields = ["profile_image", 'birth_date']
