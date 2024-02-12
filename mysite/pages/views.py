from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Student 
# def  index (response):
#     return HttpResponse("<h1>helloworld!</h1> ")

def index (request):
    students=Student.objects.all().values()
    template=loader.get_template('pages/home.html')
    context={
        'students':students,
    }
    return HttpResponse(template.render(context,request))

# def  index (response):
#     return render(response,"pages/home.html",{})

# def index(request):
#     posts=Post.objects.all()
#     return render(request,'pages/home.html',{'posts':posts})