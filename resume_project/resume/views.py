from django.shortcuts import render, redirect



def main(request):  # main page
    data = dict()
    return render(request, "main.html", data)