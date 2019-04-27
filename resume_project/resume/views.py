from random import randint

from django.contrib import messages
from django.contrib.auth import login, logout, update_session_auth_hash, authenticate
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect
from resume.API import github
from resume import models
from django.core import serializers
from django.http import JsonResponse


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
    if models.GithubConnectedUsers.objects.filter(authorid=request.user.id).exists():
        print('profile exists')
        tmp = models.GithubConnectedUsers.objects.filter(authorid=request.user.id).values()
        # tmp = tmp[0]

        return JsonResponse(list(tmp)[0], safe=False)
    else:
        github(request.user.id, request.user.last_name, request.user.username)

    return render(request, "main.html", data)


@login_required
def test_pictures(request):
    data = dict()
    if models.GithubConnectedUsers.objects.filter(authorid=request.user.id).exists():
        print('profile exists')

        data['pics'] = ['/static/users_dir/' + request.user.username + '/demo.png',
                        '/static/users_dir/' + request.user.username + '/demo2.png']

        return render(request, "plots.html", data)

    else:
        github(request.user.id, request.user.last_name, request.user.username)

    return render(request, "main.html", data)




def test_for_swift_app(request):
    data = dict()

    login_from_app = request.GET['login']
    pass_from_app = request.GET['pass']
    print(login_from_app)
    user = User.objects.get(username=login_from_app)
    if user.check_password(pass_from_app):
        return redirect("/test", request)
        tmp = models.GithubConnectedUsers.objects.filter(authorid=user.id).values()
        return JsonResponse(list(tmp)[0], safe=False)
    else:
        return JsonResponse({'id':'false'}, safe=False)


    return render(request, "main.html", data)
