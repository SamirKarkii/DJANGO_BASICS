from django.db import models
from django.db.models import Max,Min

# from datetime import date



# class Course(models.Model):
#     name = models.CharField(max_length=100)


# class Student(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()
#     address = models.TextField()
#     joined_date = models.DateField(default=date.today)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)


# Student.objects.all() #get all student #returns all rows 
# Student.objects.get(id=1) # Get one student 
# Student.objects.filter(age =30) #filters student #Gives list of matching records 




class Course(models.Model): #this is basically a a course model 
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model): #this is basically a Student mode 
    age = models.IntegerField(default=0)
    address = models.CharField(max_length=100)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name="students") #course uses a Foreignkey which means it has many to one reationship with Courese, on_delete_ ... means when a course is deleted course is deleted too.

    def __str__(self):
        return self.address

# #this is the part which feels shaky 
# Course.objects.create(name ="Python") #so name of course becomes Python
# course_obj = Course.objects.get(name="Python") #like get is used so the name is unique and the varible is assigned but why?
# Student.objects.create(age=14, address="Kathmandu",course= course_obj)  #basically this is the value of age , add, course 
# Student.objects.all() #shows all object in rows 

