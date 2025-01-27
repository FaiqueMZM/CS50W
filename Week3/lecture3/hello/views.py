from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def faique(request):
    return HttpResponse("Hello, Faique!")

def inaas(request):
    return HttpResponse(f"Hello, Inaas!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })