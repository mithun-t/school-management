from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    Department_name=models.CharField(max_length=50)
    def __str__(self):
        return self.Department_name 
    
    
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_number = models.IntegerField()
    age = models.IntegerField()
    address = models.CharField(max_length=50)


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    qualification=models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_number = models.IntegerField()
    age = models.IntegerField()
    address = models.CharField(max_length=50)
