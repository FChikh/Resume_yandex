from django.shortcuts import render, redirect



def main(request):  # main page
    data = dict()
    #data = votingEngine.friendly_extract_for_everyone()
    #return render(request, "main.html", data)