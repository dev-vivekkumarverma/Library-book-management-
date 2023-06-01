from django.db import models
from django.contrib.auth.models import User
# Create your models here.


   
        
class Student(models.Model):
    name=models.CharField(max_length=50)
    roll_number=models.CharField(max_length=50)
    course_name=models.CharField(max_length=50)
    department=models.CharField(max_length=50)
    year_of_admission=models.CharField(max_length=50)
    email_ID=models.EmailField()
    profile_picture=models.ImageField(upload_to="profile_picture/",null=True,blank=True)