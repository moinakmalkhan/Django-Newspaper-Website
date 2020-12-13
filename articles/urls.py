from django.urls import path
from . import views
urlpatterns = [
    # path("add/", views.AddArticle, name="AddArticle"),
    path("", views.FavArticle, name="FavArticle"),
    path("SaveComments/", views.SaveComments, name="savecomment"),
    path("deleteReply/", views.deleteReply, name="deleteReply"),
    path("SaveComments/<int:commentid>/",
         views.SaveComments, name="editComment"),
    path("deleteComment/", views.deleteComment, name="deleteComment"),
    path("addLikes/", views.addLikes, name="addLikes"),
    path("addToFav/", views.addToFav, name="addToFav"),
]
