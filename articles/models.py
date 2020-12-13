from django.db import models
from django.db.models.base import Model
from registration.models import ProfileSettings, User
from .manager import CustomReplyManager, CustomCommentManager


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")


class Reply(models.Model):
    comment = models.TextField(blank=True)
    objects = CustomReplyManager()
    user = models.ForeignKey(ProfileSettings, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment


class Comment(models.Model):
    comment = models.TextField(blank=True)
    objects = CustomCommentManager()
    reply = models.ManyToManyField(
        Reply, blank=True, related_name="comment_reply")
    user = models.ForeignKey(
        ProfileSettings, on_delete=models.CASCADE, blank=True, null=True)

    date_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.comment


class Articles(models.Model):
    heading = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    body = models.TextField()
    comments = models.ManyToManyField(Comment, blank=True)
    likes = models.ManyToManyField(ProfileSettings, blank=True)

    class Meta:
        verbose_name = ("Article")
        verbose_name_plural = ("Articles")

    def __str__(self):
        return self.body


class FavCategory(models.Model):
    user = models.ForeignKey(ProfileSettings, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
