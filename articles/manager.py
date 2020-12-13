from django.db import models


class CustomReplyManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by("date_time")


class CustomCommentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by("date_time")

    # def get_roll_range(self, from_, to):
    #     return super().get_queryset().filter(roll__range=(from_, to))
