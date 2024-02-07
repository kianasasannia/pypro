from django.shortcuts import render
from django.http import HttpResponse


# def  index (response):
#     return HttpResponse("<h1>helloworld!</h1> ")

def  index (response):
    return render(response,"pages/home.html",{})