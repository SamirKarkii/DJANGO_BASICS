# # from django.shortcuts import render
# # from django.http import HttpResponse
# # from .models import Student

# # def home(request):
# #     data = {
# #         'name':'samir',
# #         'age': '21'
# #     }
    
# #     return render(request,'home.html',data)

# # def about(request):
# #     return HttpResponse("We’re passionate about building simple, powerful web applications with Django. Our goal is to make learning and development smooth, fun, and practical  for everyone. With clean design and clear code, we turn ideas into working projects effortlessly.")

# # def students(request):
# #     return HttpResponse("This view describes about student")

# # def student(request):
# #     data = Student.objects.all()
# #     return render(request,'students.html', {'students':data})

# # from django.http import HttpResponse 




# from django.http import HttpResponse
# from .models import Student,Course


# # def home(request): 
# #     return HttpResponse("Hello Django")

# # def student_list(request):

# #     students = Student.objects.all()
# #     student_name = []
# #     for student in students:
# #         student_name.append(student.address)

# #     return HttpResponse(",".join(student_name))

# # def student_detail(request, id):
# #     student = Student.objects.get(id=id) # id =1

# #     return HttpResponse(student.address)

# # #Read 
# def student_list(request):
#     students= Student.objects.all()
#     data = []
#     for s in students:
#         data.append(f'{s.id}-{s.address}')
#     return HttpResponse(",".join(data))

# # #Create 
# def create_student(request, age, address, course_id):
#     course = Course.objects.get(id=course_id)

#     Student.objects.create(
#         age=age,
#         address=address,
#         course=course
#     )

#     return HttpResponse("Student created")

# # #Update
# def update_student(request,id,new_address):
#     student  = Student.objects.get(id=id)
#     student.address = new_address
#     student.save() #this tells django to save the object in the databasee!!

#     return HttpResponse("Student updated ")

# # #Delete 
# def delete_student(request,id):
#     student = Student.objects.get(id=id)
#     student.delete()
#     return HttpResponse("Student deleted")



# from django.views import View
# from django.http import HttpResponse
# from .models import Student,Course


# #Simple Classed Based Views 
# class StudentListView(View):
#     def get(self,request):
#         students = Student.objects.all()

#         data = []
#         for s in students:
#             data.append(f"{s.address}-{s.id}")
#         return HttpResponse(",".join(data))


# #Generic 
# from django.views.generic import ListView
# from .models import Student

# class StudentListView(ListView):
#     model = Student


# #Mixin
# from .models import Student
# from django.http import HttpRequest
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views import View
# from django.views.generic import ListView

# # class StudentListView(LoginRequiredMixin,ListView):
# #     model = Student





# from django.views import View
# from django.http import HttpResponse
# from .models import Student

# class StudentDetaiView(View):
#     def get(self,request,id):
#         try: 
#             student = Student.objects.get(id=id)

#             data = f'{student.id}-{student.address}-{student.age}'
#             return HttpResponse(data)
        
#         except Student.DoesNotExist:
#             return HttpResponse("Student not found suiii")


# from django.views import View
# from django.http import HttpResponse
# from .models import Student,Course

# class StudentCreateView(View):
#     def post(self,request):
#         a = Course.objects.first()
#         Student.objects.create(age=10,address="Bisbain",course=a)

#         return HttpResponse("Student Created")


# from django.views import View
# from .models import Student
# from django.http import HttpResponse

# class SearchStudentView(View):
#     def get(self, request):

#         address_from_url = request.GET.get("address")

#         print("INPUT FROM URL:", repr(address_from_url))

#         data = Student.objects.filter(address__icontains=address_from_url)

#         print("RESULT:", list(data))

#         return HttpResponse(
#             ", ".join([s.address for s in data]) if data else "No match found"
#         )

# from django.views import View
# from django.http import HttpResponse
# from .models import Student

# # class StudentSearchView(View):
# #     def get(self, request):
# #         address = request.GET.get("address")

# #         students = Student.objects.filter(address=address)

# #         return HttpResponse(students)

# from django.views import View
# from django.http import HttpResponse
# from .models import Student, Course
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt

# from django.views import View
# from django.http import HttpResponse
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt

# from .models import Student, Course

# @method_decorator(csrf_exempt, name='dispatch')
# class CreateStudent(View):

#     def post(self, request):

#         age = request.POST.get("age")
#         address = request.POST.get("address")
#         course_id = request.POST.get("course_id")

#         try: 
#             selected_course = Course.objects.get(id=course_id)
#             Student.objects.create(
#                 age = age,
#                 address = address,
#                 course = selected_course
#             )
#             return HttpResponse("Student Successfully Created")
        
#         except Course.DoesNotExist:
#             return HttpResponse("Course Not found mate")


# from django.views import View
# from django.http import HttpResponse
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt

# from .models import Student, Course
# @method_decorator(csrf_exempt, name='dispatch')
# class UpdateStudent(View):
#     def post(self,request,id):
#         try:
#             student = Student.objects.get(id=id)
#         except Student.DoesNotExist:
#             return HttpResponse("Student Not Found")
        
#         new_address = request.POST.get("address")
#         if new_address: 
#             student.address = new_address
#             student.save ()

#             return HttpResponse("Student Updated")
        
#         return HttpResponse("No address  provided ")

# from django.views import View
# from .models import Student,Course
# from django.http import HttpResponse
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt

# @method_decorator(csrf_exempt, name='dispatch')
# class DeleteStudent(View):
#     def delete(self,request,id):
#         try:
#             student = Student.objects.get(id=id)
#         except Student.DoesNotExist:
#             return HttpResponse("Student doesnot exist")
#         student.delete()
#         return HttpResponse("Student Deleted")