from django.db import models
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




class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    age = models.IntegerField(default=0)
    address = models.CharField(max_length=100)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)

# Course.objects.create(name ="Python")
# course_obj = Course.objects.get(name="Python")
# Student.objects.create(age=14, address="Kathmandu", course_obj")
# Student.objects.all()