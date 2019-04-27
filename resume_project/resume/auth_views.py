from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.urls import NoReverseMatch

from resume.forms import RegistrationForm, LoginForm

def signin_site_page(request):
    context = dict()
    next_page = request.GET.get('next', '/')
    username = password = ''
    context['next'] = next_page
    context['login_error'] = 0

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
                form = LoginForm()
                messages.error(request, 'Пользователь неактивен')
                context['form'] = form
                return render(request, 'signin_site.html', context)
        else:
            form = LoginForm()
            context['login_error'] = 1
            messages.error(request, 'Неверные логин или пароль')
            context['form'] = form
    return render(request, 'signin_site.html', context)


def register(request):
    next_page = request.GET.get('next', '')
    context = dict()
    context['title'] = 'Регистрация'
    context['password_match'] = 1
    context['invalid_form'] = 0
    context['user_exists'] = 0

    if request.method == "GET":
        context['form'] = RegistrationForm()
    elif request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.data.get('password') != form.data.get('re_password'):
            context['password_match'] = 0
        if form.is_valid():
            try:
                user = User.objects.create_user(
                    username=form.data.get('username'),
                    email=form.data.get('email'),
                    password=form.data.get('password'),
                    last_name=form.data.get('github_username')
                )

            except IntegrityError:
                context['user_exists'] = 1
                messages.error(request, 'Пользователь с таким логином уже существует')
                return render(request, 'registration.html', context)
            else:
                user.save()
                login(request, user)
                try:
                    return redirect(next_page)
                except NoReverseMatch:
                    return redirect('/')
        else:
            if form.data.get('password') == form.data.get('re_password'):
                context['invalid_form'] = 1
            context['form'] = form

    return render(request, 'registration.html', context)
