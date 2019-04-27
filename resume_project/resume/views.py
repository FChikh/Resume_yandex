from random import randint

from django.contrib import messages
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect
from resume.API import github
from resume import models

@login_required
def main(request):  # main page
    data = dict()
    return render(request, "main.html", data)

def logout_func(request):
    logout(request)
    return redirect('/login/?next=/')

@login_required
def test(request):
    data = dict()
    if models.GithubConnectedUsers.objects.filter(authorid = request.user.id).exists():
        print('profile exists')
    else:
        github(request.user.id,request.user.last_name, request.user.username)


    return render(request, "main.html", data)
