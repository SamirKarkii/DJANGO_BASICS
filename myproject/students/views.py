# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import Student

# def home(request):
#     data = {
#         'name':'samir',
#         'age': '21'
#     }
    
#     return render(request,'home.html',data)

# def about(request):
#     return HttpResponse("We’re passionate about building simple, powerful web applications with Django. Our goal is to make learning and development smooth, fun, and practical  for everyone. With clean design and clear code, we turn ideas into working projects effortlessly.")

# def students(request):
#     return HttpResponse("This view describes about student")

# def student(request):
#     data = Student.objects.all()
#     return render(request,'students.html', {'students':data})

# from django.http import HttpResponse 




from django.http import HttpResponse
from .models import Student

def home(request): 
    return HttpResponse("Hello Django")

def student_list(request):

    students = Student.objects.all()
    student_name = []
    for student in students:
        student_name.append(student.address)

    return HttpResponse(",".join(student_name))

def student_detail(request, id):
    student = Student.objects.get(id=id) # id =1

    return HttpResponse(student.address)