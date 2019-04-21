from random import randint

from django.contrib import messages
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect


@login_required
def main(request):  # main page
    data = dict()
    return render(request, "main.html", data)