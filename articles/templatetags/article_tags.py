from django import template
from registration import models
from articles.models import FavCategory, Category
register = template.Library()


@register.simple_tag
def like_unlike_btn(likes, userid):
    if userid == None:
        return "Like"
    else:
        user = models.User.objects.get(pk=userid)
        user = models.ProfileSettings.objects.get(user=user)
        for i in likes.all():
            if i.user.id == user.user.id:
                return "UnLike"
        return "Like"


@register.simple_tag
def add_category(category, userid):
    if userid == None:
        return "Add to favorite"
    else:
        user = models.User.objects.get(pk=userid)
        user = models.ProfileSettings.objects.get(user=user)
        try:
            FavCategory.objects.get(user=user, category=category)
            return "Remove from favorite"
        except:
            return "Add to favorite"
