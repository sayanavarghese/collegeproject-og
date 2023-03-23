from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Job(models.Model):
    title=models.TextField(max_length=225)
    position=models.TextField(max_length=225)
    category=models.TextField(max_length=225)
    location=models.TextField(max_length=225)
    description=models.TextField(max_length=225)
    userld=models.IntegerField()
    salary=models.TextField(max_length=225)
    Create_at=models.DateTimesField(auto_now_add=True)
    
class Resume(models.Model):
    title=models.TextField(max_length=225)
    name=models.TextField(max_length=225)
    email=models.EmailField(max_length=225)
    address=models.TextField(max_length=225)
    experiance=models.TextField(max_length=225)
    qualification=models.TextField(max_length=225)
    phone_no=models.IntegerField(max_length=12)
    about_me=models.TextField(max_length=225)
class Application(models.Model):
        applied_by=models.Forignkey(User,on_delete=models.CASCADE)
        job=models.models.Forignkey(User,on_delete=models.CASCADE)
        Create_at=models.DateTimesField(auto_now_add=True)

class Profile(models.Model):
        CHOICES = (
        ("ADMIN", "ADMIN"),
        ("JOB_ADDER", "JOB_ADDER"),
        ("USER", "USER"),
)
        user =models.OneToOneField(User, on_delete= models.CASCADE)
        user_type =models.CharField(max_length=150, choices =CHOICES, default ='USER')



    

    