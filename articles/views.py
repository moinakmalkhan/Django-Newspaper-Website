from django.shortcuts import redirect, render
# from .forms import ArticleForm
from django.http import JsonResponse
from .models import *
from django.contrib.auth.models import User
from registration.models import ProfileSettings


def HomeArticle(request):
    articles = Articles.objects.all()
    context = {
        "articles": articles,
    }
    return render(request, "articles/articles.html", context)


def FavArticle(request):
    user = request.user.id
    articles = []
    if user:
        user = User.objects.get(id=user)
        try:
            # if we create admin user by typing 'python manage.py createsuperuser' then following statement will raise exception because we did not create object of ProfileSetting
            user = ProfileSettings.objects.get(user=user)
        except:
            return redirect("ProfileSetting")
        cate = FavCategory.objects.filter(user=user)
        for i in cate:
            art = Articles.objects.filter(category=i.category)
            for j in art:
                # here we are walk through all the object of FavCategory and appending it into a list
                articles.append(j)
    context = {
        "articles": articles,
    }
    return render(request, "articles/articles.html", context)


def addToFav(request):
    if request.method == "POST":
        categoryid = request.POST['categoryid']
        action = (request.POST['action']).replace(' ', "")
        action = action.replace("\n", "")
        userid = request.user.id
        if userid != None and userid != "None":
            user = User.objects.get(id=userid)
            try:
                user = ProfileSettings.objects.get(user=user)
            except:
                return redirect("ProfileSetting")
            category = Category.objects.get(pk=categoryid)
            try:
                # if we successfully get object of FavCategory its mean this catetory is already added into FavCategory we should delete it. if not then following statement will raise exception and we should add it
                fc = FavCategory.objects.get(user=user, category=category)
                fc.delete()
            except:
                if action == "Addtofavorite":
                    fc = FavCategory(user=user, category=category)
                    fc.save()

            return JsonResponse({"status": "Save"})
        else:
            return JsonResponse({"status": 404, "error": "Please login before like Category"})


def addLikes(request):
    if request.method == "POST":
        # adding like
        articleid = request.POST['articleid']
        action = str(request.POST['action']).replace(" ", "")
        action = action.replace("\n", "")
        userid = request.user.id
        if userid != None and userid != "None":
            user = User.objects.get(id=userid)
            try:
                user2 = ProfileSettings.objects.get(user=user)
            except:
                return redirect("ProfileSetting")
            # get article object to add like
            article = Articles.objects.get(pk=articleid)
            if action == 'Like':
                # adding like to many to many relation with article
                article.likes.add(user2)
            else:
                # removing like to many to many relation with article
                article.likes.remove(user2)
            article.save()
            return JsonResponse({"status": "Save"})
        else:
            return JsonResponse({"status": 404, "error": "Please login before like post"})


def deleteReply(request):
    if request.method == "POST":
        replyid = int(request.POST['replyid'])
        commentid = int(request.POST['commentid'])
        rep = Reply.objects.get(pk=replyid)
        if (rep.user.user.id == request.user.id):
            cm = Comment.objects.get(pk=commentid)
            # removing reply from many to many relation with comment
            cm.reply.remove(rep)
            cm.save()
            rep.delete()
            return JsonResponse({"status": 200})
        else:
            return JsonResponse({"status": 403, "error": "You cannot delete this comment"})


def deleteComment(request):
    if request.method == "POST":
        # delete comment
        commentid = int(request.POST['commentid'])
        cm = Comment.objects.get(pk=commentid)
        replyid = []
        if (cm.user.user.id == request.user.id):

            for i in cm.reply.all():
                # Here we walk through all the reply of comment which we are going to delete and delete them
                replyid.append(i.id)
                cm.reply.remove(i)
                i.delete()
            cm.delete()
            return JsonResponse({"status": 200, "commentid": commentid, "replyid": replyid})
        else:
            return JsonResponse({"status": 403, "error": "You cannot delete this comment."})


def SaveComments(request, commentid=None):
    if request.method == "POST":
        data = request.POST
        article = int(data.get('article', 0))
        try:
            # if user = "None" then it cannot be convert into int
            userid = int(data.get('user', request.user.id))
        except:
            userid = 0
        reply_or_comment_id = int(data.get('commentid', 0))
        if userid == request.user.id or not userid and commentid:
            comment = data['comment']
            if userid:
                # get our custom user from our custom user model
                user = User.objects.get(id=userid)
                try:
                    # if we create admin user by typing 'python manage.py createsuperuser' then following statement will raise exception because we did not create object of ProfileSetting
                    user2 = ProfileSettings.objects.get(user=user)
                except:
                    return redirect("ProfileSetting")
            if commentid:
                # when commentid variable is not None we should update object
                if reply_or_comment_id:
                    # updating reply object
                    rp = Reply.objects.get(id=reply_or_comment_id)
                    if rp.user.user.id == userid:
                        rp.comment = comment
                        rp.save()
                    else:
                        return JsonResponse({"status": 404, "error": "You cannot delete/edit this data."})
                else:
                    # updating comment object
                    cm = Comment.objects.get(pk=commentid)
                    if cm.user.user.id == userid:
                        cm.comment = comment
                        cm.save()
                    else:
                        return JsonResponse({"status": 404, "error": "You cannot delete/edit this data."})
            else:
                # when commentid variable is None we have to create object
                if reply_or_comment_id:
                    # creating reply object
                    cm = Comment.objects.get(pk=reply_or_comment_id)
                    rp = Reply(user=user2, comment=comment)
                    rp.save()
                    reply_or_comment_id = rp.id
                    # adding repy with many to many relation with coment
                    cm.reply.add(rp)
                    cm.save()
                else:
                    # creating comment object
                    cm = Comment(id=commentid, user=user2, comment=comment)
                    cm.save()

            context = {
                "status": "Save",
            }
            if user and not commentid:
                # adding comment into many to many relation with article
                art = Articles.objects.get(id=article)
                art.comments.add(cm)
                art.save()

                commentid = cm.id

            img = user2.profile_image.url
            username = user.username
            context['img'] = img
            context['username'] = username
            context['replyid'] = reply_or_comment_id
            context['comment'] = comment
            context['commentid'] = commentid
            context['articleid'] = article
            return JsonResponse(context)
        else:
            return JsonResponse({"status": 404, "error": "You cannot add/edit data."})

    return render(request, "articles/articles.html")
