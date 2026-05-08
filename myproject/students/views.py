from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

def home(request):
    data = {
        'name':'samir',
        'age': '21'
    }
    
    return render(request,'home.html',data)

def about(request):
    return HttpResponse("We’re passionate about building simple, powerful web applications with Django. Our goal is to make learning and development smooth, fun, and practical  for everyone. With clean design and clear code, we turn ideas into working projects effortlessly.")

def students(request):
    return HttpResponse("This view describes about student")

def student(request):
    data = Student.objects.all()
    return render(request,'students.html', {})

