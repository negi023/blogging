from django.shortcuts import render, redirect
from .forms import Registrationform, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import (login,
                                 logout,
                                 update_session_auth_hash)
from django.contrib.auth.decorators import login_required
from articles.models import Articles
from django.contrib.auth.models import User


def home(request):
    articles = Articles.objects.all()
    context = {'articles': articles}
    return render(request, 'account/homepage.html', context)


def signup(request):
    if request.method == 'POST':
        form = Registrationform(request.POST or None)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = Registrationform()
    return render(request, 'account/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST or None)  # request.POST is not the first parameter
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required()
def editProfile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('showprofile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user)
        context = {'u_form': u_form,
                   'p_form': p_form}
    return render(request, 'account/editprofile.html', context)


def showProfile(request):
    return render(request, 'account/showProfile.html')

def deleteProfile(request,id):
    User.objects.get(id=id).delete()
    return redirect('home')

@login_required()
def changepass(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST or None, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('showprofile')
        else:
            return redirect('changepass')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'account/passwordchange.html', {'form': form})
