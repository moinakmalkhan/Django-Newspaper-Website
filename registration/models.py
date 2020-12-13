from django.db import models
from django.contrib.auth.models import User
import time


class ProfileSettings(models.Model):
    profile_image = models.ImageField(
        upload_to="ProfileImages/", default="/ProfileImages/noImage.jpg")
    birth_date = models.DateField(default=time.strftime("%Y-%m-%d"))
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("ProfileSettings")
        verbose_name_plural = ("ProfileSettings")
