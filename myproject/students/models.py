from django.db import models
from datetime import date
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.TextField()
    joined_date = models.DateField(default=date.today)


Student.objects.all() #get all student #returns all rows 
Student.objects.get(id=1) # Get one student 
Student.objects.filter(age =30) #filters student #Gives list of matching records 
