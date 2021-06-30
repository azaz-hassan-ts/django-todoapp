from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, "hi\index.html")


def azaz(request):
    return HttpResponse("Hi Azaz")


def greet(request, name):
    return render(request, "hi/greet.html", {
        "name": name.capitalize()
    })
