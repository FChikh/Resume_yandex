from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.urls import NoReverseMatch

from resume.forms import reg_logForm


def signin_site_page(request):
    context = dict()
    next_page = request.GET.get('next', '/')
    username = password = ''
    context['next'] = next_page

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                try:
                    return redirect(next_page)
                except NoReverseMatch:
                    return redirect('/')
            else:
                form = reg_logForm()
                messages.error(request, 'Пользователь неактивен')
                context['form'] = form
                return render(request, 'signin_site.html', context)
        else:
            form = reg_logForm()
            messages.error(request, 'Неверные логин или пароль')
            context['form'] = form
            return render(request, 'signin_site.html', context)
    return render(request, 'signin_site.html', context)


def register(request):
    next_page = request.GET.get('next', '')
    context = dict()
    context['title'] = 'Регистрация'

    if request.method == "GET":
        context['form'] = reg_logForm()
    elif request.method == "POST":
        form = reg_logForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.create_user(
                    username=form.data.get('username'),
                    email=form.data.get('email'),
                    password=form.data.get('password'),
                )
            except IntegrityError:
                messages.error(request, 'Пользователь с таким логином уже существует')
                return render(request, 'registraion.html', context)
            else:
                user.save()
                login(request, user)
                try:
                    return redirect(next_page)
                except NoReverseMatch:
                    return redirect('/')
        else:
            context['form'] = form

    return render(request, 'registration.html', context)
