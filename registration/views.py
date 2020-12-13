from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, ProfileSettingsForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .models import ProfileSettings
from django.core.mail import EmailMultiAlternatives
import os


@login_required(login_url='/accounts/login/')
def profile(request):
    user = User.objects.get(pk=request.user.id)
    try:
        user = ProfileSettings.objects.get(user=user)
    except:
        return redirect("ProfileSetting")
    return render(request, "registration/profile.html", {"user": user})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            firstname = form.cleaned_data.get('first_name')
            raw_password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            user = authenticate(username=username, password=raw_password)
            data = ProfileSettings(user=user)
            data.save()
            login(request, user)
            subject, from_email, to = 'Welcome', (os.environ['my_email']), [
                email]
            text_content = ""
            html_content = f"""<h2>Welcome {firstname.title()} to our newspaper website.</h2>
                <p>Thank you for registration</p>
            """
            msg = EmailMultiAlternatives(subject, text_content, from_email, to)
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return redirect('ProfileSetting')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required(login_url='/accounts/login/')
def ProfileSetting(request):
    if request.method == 'POST':
        user = User.objects.get(pk=request.user.id)
        form = ProfileSettingsForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                data = ProfileSettings.objects.get(user=user)
                data.profile_image = form.cleaned_data['profile_image']
                data.birth_date = form.cleaned_data['birth_date']
                data.save()
            except:
                m = ProfileSettings(
                    birth_date=form.cleaned_data['birth_date'], profile_image=form.cleaned_data['profile_image'], user=user)
                m.save()
                # form.save()
            return redirect('profile')
    else:
        form = ProfileSettingsForm()

    return render(request, 'registration/profileSettings.html', {'form': form, })


def signin(request):
    if request.method == "GET":
        fm = SignUpForm()
        context = {"form": fm}
        return render(request, "registration/signin.html", context)
    return render(request, "registration/signin.html")
